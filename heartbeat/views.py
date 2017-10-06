from django.shortcuts import render
from django.http import JsonResponse
import json
import time

# Create your views here.
def index(request):
    context={
    }
    return render(request,"heartbeat/index2.html",context)

def investment_analyzer(request):
    context={
    }
    return render(request,"heartbeat/index3.html",context)


def withdraw_analyzer(request):
    context={
    }
    return render(request,"heartbeat/index4.html",context)

def demo_dashboard(request):
    context={
    }
    return render(request,"heartbeat/demo_dashboard.html",context)

counter = 0
import random
def get_data(request):
    global counter
    counter = counter+1
    #int(time.time())*1000
    context={
        'arr': [counter,random.randint(70,80)],
        'arr2': [counter, random.randint(40, 50)]

    }
    return JsonResponse(json.loads(json.dumps(context)))
