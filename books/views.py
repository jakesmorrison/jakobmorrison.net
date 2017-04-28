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
import os
from collections import OrderedDict

from .management import config as cfg
from jakobmorrison.settings import BASE_DIR

vector_path = os.path.join(BASE_DIR, 'books/static/books/vector/')
nltk_path = os.path.join(BASE_DIR, 'books/static/books/nltk/')


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
    df_lookup = df

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
        print(n)
        html_table = html_table.replace(n , "<a class=\"mylink\" href=\"#\">"+n+"</a>", 1)
        print(html_table)


    lookup = df_lookup[df_lookup["Title"] == book_names[len(book_names)-1]]
    lookup = lookup["Lookup"].tolist()[0]

    context = {
        "default" : book_names[len(book_names)-1],
        "html_table": html_table,
        "title": df_display['Title'].tolist(),
        "date": [str(dt) for dt in df_display['Date_Start'].tolist()],
        "lookup":lookup
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
    lookup = df[df["Title"] == book]
    lookup = lookup["Lookup"].tolist()[0]


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

    piechart = []
    for x in ([tuple(x) for x in df[["Title","Word_Count","Type"]].values]):
        if x[2] == "Fiction":
            foo = {"text":x[0],"value":x[1],"color":"rgba(0,153,255,.5)"}
        else:
            foo = {"text":x[0],"value":x[1],"color":"rgba(144,153,255,1)"}
        piechart.append(foo)

    context = {
        "book": book,
        "cat": cfg.CAT,
        "series": cfg.SERIES,
        "scatter": new_scatter,
        "regression": new_reg,
        "word_cloud": word_cloud_new,
        "lookup": lookup,
        "piechart": piechart
    }
    return JsonResponse(json.loads(json.dumps(context)))

def vector_chart(request):
    params = request.GET
    book = (params["Title"])
    lookup = (params["lookup"])

    # Creating vector plot
    from nltk.corpus import wordnet as wn
    import nltk
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

    df_vector = pd.read_pickle(os.path.join(vector_path,lookup+".pkl"))
    vector_word =df_vector["word"]
    x_word = df_vector["x"]
    y_word = df_vector["y"]

    a_arr = []
    r_arr = []
    n_arr = []
    v_arr = []
    s_arr = []
    q_arr = []

    for x in range(0,len(vector_word)):
        t = wn.synsets(vector_word[x])
        try:
            t = (t[0].pos())
        except:
            t = "?"

        if t == "a":
            # a_arr.append([x_word[x],y_word[x],vector_word[x]])
            a_arr.append({'fillColor': 'blue','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        elif t == "r":
            # r_arr.append([x_word[x],y_word[x],vector_word[x]])
            r_arr.append({'fillColor': 'black','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        elif t == "n":
            # n_arr.append([x_word[x],y_word[x],vector_word[x]])
            n_arr.append({'fillColor': '#90ed7d','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        elif t == "v":
            # v_arr.append([x_word[x],y_word[x],vector_word[x]])
            v_arr.append({'fillColor': 'orange','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        elif t == "s":
            # s_arr.append([x_word[x],y_word[x],vector_word[x]])
            s_arr.append({'fillColor': 'purple','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        elif t == "?":
            # q_arr.append([x_word[x],y_word[x],vector_word[x]])
            q_arr.append({'fillColor': 'red','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})
        # vector_scatter.append({'fillColor': 'black','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})

    vector_scatter = [{'name':'Adjective','data':a_arr},
                      {'name':'Adverb','data':r_arr},
                      {'name': 'Noun', 'data': n_arr},
                      {'name': 'Verb', 'data': v_arr},
                      {'name': 'Adjective Sat', 'data': s_arr},
                      {'name': '?', 'data': q_arr}]


    context = {
        "book": book,
        "vector_scatter": vector_scatter
    }
    return JsonResponse(json.loads(json.dumps(context)))

def all_book_vector_chart(request):
    print("test")
    # Creating vector plot
    from nltk.corpus import wordnet as wn
    import nltk
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

    df_vector = pd.read_pickle(os.path.join(vector_path,"all_books.pkl"))
    vector_word =df_vector["word"]
    x_word = df_vector["x"]
    y_word = df_vector["y"]

    vector_scatter = []
    for x in range(0,len(vector_word)):
        t = wn.synsets(vector_word[x])
        try:
            t = (t[0].pos())
        except:
            t = "?"

        if t == "a":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'red','name': vector_word[x] +" (Adjective)", 'x': x_word[x], 'y': y_word[x]})
        elif t == "r":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'blue','name': vector_word[x] +" (Adverb)", 'x': x_word[x], 'y': y_word[x]})
        elif t == "n":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'green','name': vector_word[x] +" (Noun)", 'x': x_word[x], 'y': y_word[x]})
        elif t == "v":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'purple','name': vector_word[x] +" (Verb)", 'x': x_word[x], 'y': y_word[x]})
        elif t == "s":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'orange','name': vector_word[x] +" (Adjective Sat)", 'x': x_word[x], 'y': y_word[x]})
        elif t == "?":
            vector_scatter.append({'id':vector_word[x],'fillColor': 'black','name': vector_word[x] +" (?)", 'x': x_word[x], 'y': y_word[x]})
        # vector_scatter.append({'fillColor': 'black','name': vector_word[x], 'x': x_word[x], 'y': y_word[x]})

    context = {
        "vector_scatter": vector_scatter
    }
    return JsonResponse(json.loads(json.dumps(context)))
