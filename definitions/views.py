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
    Config.current_context = context
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

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializer import WordsSerializer

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def words_list(request):
    if request.method == 'GET':
        w = Words.objects.all()
        print(w)
        serializer = WordsSerializer(w, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def words_current(request):
    if request.method == 'GET':
        w = Config.current_context
        return Response(w)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def words_detail(request, pk1, pk2):
    try:
        w = Words.objects.all().filter(**{pk1:pk2}).values()
    except Words.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordsSerializer(w, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordsSerializer(w, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        w.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Config(object):
    current_context = {}

