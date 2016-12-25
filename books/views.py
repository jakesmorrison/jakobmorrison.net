from django.shortcuts import render

from .management import config as cfg
from .management import methods
from django.http import JsonResponse
from collections import Counter

import json
import pandas as pd
import numpy as np
cfg = cfg.Config

import os
from jakobmorrison.settings import BASE_DIR
book_path = os.path.join(BASE_DIR, 'books/static/books/book_list/')

# Create your views here.

def home(request):
    cfg.SERIES=[]
    df = pd.DataFrame(cfg.BOOK_LIST)
    df_display = df.drop("lookup",1)
    cols  = "Title,Author,Type,Genre,Date Start,Date Finish,Word Count,Unique Words,Vocab Density".split(",")
    df_display = df_display[cols]
    book_names = df_display["Title"].tolist()

    html_table = df_display.to_html(index=False, classes='table table-striped table-bordered table-hover table-responsive')
    for n in book_names:
        html_table = html_table.replace(n ,  "<a class=\"mylink\" href=\"#\">"+n+"</a>")

    context = {
        "default" : book_names[0],
        "html_table": html_table,
    }
    return render(request, 'books/home.html', context)


def quick_chart(request):
    params = request.GET
    book = (params["Title"])
    df = pd.DataFrame(cfg.BOOK_LIST)
    lookup_val = df[df["Title"] == book]["lookup"]
    lookup_val = lookup_val.tolist()[0]
    book_dir = book_path
    book_file = open(book_dir + str(lookup_val), 'r')
    book_string = methods.Book_Methods.clean_up(book_file)
    words, unique_words, vocab_density = methods.Book_Methods.get_stats(book_string)

    word_length = []
    for w in words:
        word_length.append(len(w))

    word_length = Counter(word_length)
    word_length = sorted(word_length.items())
    word_length, frequency = zip(*word_length)
    probablity = [x / len(words) for x in frequency]

    word_cloud = methods.Book_Methods.word_cloud(words)

    if cfg.SERIES:
        cfg.SERIES = cfg.SERIES+[{'name':book, 'data':probablity}]
        list_of_books = []
        temp = []
        for x in cfg.SERIES:
            if x["name"] in list_of_books:
                pass
            else:
                temp.append(x)
            list_of_books.append(x["name"])
        cfg.SERIES = temp
        bins = list(set(cfg.CAT+list(word_length)))
        bins = np.linspace(bins[0], bins[-1], bins[-1])
        cfg.CAT = list(bins)
    else:
        cfg.SERIES = [{'name':book, 'data':probablity}]
        cfg.CAT = list(word_length)


    scatter_data = [list(a) for a in zip(df["Word Count"].tolist(), df["Vocab Density"].tolist())]
    new_scatter = []
    for n,x in enumerate(scatter_data):
        new_scatter.append({'name': df["Title"].tolist()[n], 'x': float("%.2f"%x[0]), 'y': float("%.2f"%x[1])})

    x, y = zip(*scatter_data)
    reg = methods.Book_Methods.calculate_regresssion(x,y,max(df["Word Count"].tolist()))
    new_reg = []
    for n,x in enumerate(reg):
        new_reg.append([float("%.2f"%x[0]), float("%.2f"%x[1])])

    context = {
        "book": book,
        "cat": cfg.CAT,
        "series": cfg.SERIES,
        "scatter": new_scatter,
        "regression": new_reg,
        "word_cloud": word_cloud
    }
    return JsonResponse(json.loads(json.dumps(context)))

