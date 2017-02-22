from django.shortcuts import render

from .management import config as cfg
from .management import methods
from django.http import JsonResponse
from collections import Counter

from .models import Books

import json
import pandas as pd
import numpy as np
import re

from .management import config as cfg
cfg = cfg.Config
cfg.SERIES=[]
cfg.CAT = []

# Create your views here.
def home(request):
    db_books = Books.objects.all()
    df = pd.DataFrame()
    for x in db_books.values():
        df_temp = pd.DataFrame.from_dict(dict(x.items()), orient='index')
        df = df.append(df_temp.T, ignore_index=True)

    df_display = df.drop("Lookup",1)
    df_display = df_display.drop("id",1)
    df_display = df_display.drop("Unique_Word_list",1)
    df_display = df_display.drop("Occurance_Dict",1)
    df_display = df_display.sort_values(by='Date_Start')

    cols  = "Title,Author,Type,Genre,Date_Start,Date_Finish,Word_Count,Sentence_Count,Word_Per_Sentence,Unique_Words," \
            "Average_Unique_Word_Length,Vocab_Density".split(",")
    df_display = df_display[cols]
    book_names = df_display["Title"].tolist()

    html_table = df_display.to_html(index=False, classes='table table-striped table-bordered table-hover table-responsive'  )
    for n in book_names:
        html_table = html_table.replace(n ,  "<a class=\"mylink\" href=\"#\">"+n+"</a>")

    context = {
        "default" : book_names[len(book_names)-1],
        "html_table": html_table,
        "title": df_display['Title'].tolist(),
        "date": [str(dt) for dt in df_display['Date_Start'].tolist()]
    }
    return render(request, 'books/home.html', context)


def quick_chart(request):
    params = request.GET
    book = (params["Title"])

    # Converting db into df and dropping columns that arent needed.
    db_books = Books.objects.all()
    df = pd.DataFrame()
    for x in db_books.values():
        df_temp = pd.DataFrame.from_dict(dict(x.items()), orient='index')
        df = df.append(df_temp.T, ignore_index=True)
    df = df.drop("Lookup",1)
    df = df.drop("id",1)

    # Getting specific book details
    df_book = df[df["Title"] == book]

    # Need to un json dumps the data
    words = json.loads(df_book["Unique_Word_list"].tolist()[0])
    histo = dict(Counter(words))

    # Saving Series to config file
    my_sum = sum(list(histo.values()))
    cdf = [x/my_sum for x in list(histo.values())]
    cfg.SERIES = [{'name':book, 'data':cdf}]
    cfg.CAT = list(histo.keys())


    # Creating scatter plot plot
    scatter = list(zip(df["Word_Count"].tolist(), df["Vocab_Density"].tolist()))
    scatter_data = [list(a) for a in scatter]
    new_scatter = []
    for n,x in enumerate(scatter_data):
        new_scatter.append({'name': df["Title"].tolist()[n], 'x': float("%.2f"%x[0]), 'y': float("%.2f"%x[1])})

    # Creating Regression Line
    x, y = zip(*scatter_data)
    reg = methods.Book_Methods.calculate_regresssion(x,y,max(df["Word_Count"].tolist()))
    new_reg = []
    for n,x in enumerate(reg):
        new_reg.append([float("%.2f"%x[0]), float("%.2f"%x[1])])

    # word cloud
    word_cloud = json.loads(df_book["Occurance_Dict"].tolist()[0])

    word_cloud_new = []
    for x in word_cloud:
        key, value = list(x.items())[0]
        word_cloud_new.append({'text':key,'weight':value})

    context = {
        "book": book,
        "cat": cfg.CAT,
        "series": cfg.SERIES,
        "scatter": new_scatter,
        "regression": new_reg,
        "word_cloud": word_cloud_new
    }
    return JsonResponse(json.loads(json.dumps(context)))

