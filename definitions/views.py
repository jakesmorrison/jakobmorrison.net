from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Words
import random

from PyDictionary import PyDictionary

# Create your views here.

def home(request):
    def_table = list((Words.objects.values()))
    random.shuffle(def_table)
    word = def_table[0]['word']
    type = def_table[0]['type']
    definition = def_table[0]['definition']
    definition = definition.split("\n")

    dictionary_count = ([x["word"] for x in Words.objects.values()])

    context = {
        "word": word,
        "type": type,
        "definition": definition,
        "dictionary_count": len(dictionary_count),
        "id_count": dictionary_count.index(word),
    }
    return render(request, 'definitions/home.html', context)

def add_to_db(request):
    dictionary = PyDictionary()
    params = request.GET
    words= params["word"]
    words = words.split(",")
    for word in words:
        definition = dictionary.meaning(word)
        try:
            t = (", ".join(list(definition.keys())))
            mydef = ("\n".join(list(definition.values())[0]))
        except:
            t = ""
            mydef = ""

        if word in [x["word"] for x in Words.objects.values()]:
            pass
        else:
            s = Words(
                word=word[0].upper()+word[1:],
                type=t,
                definition=mydef,
                frequency=0,
            )
            s.save()
    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))
