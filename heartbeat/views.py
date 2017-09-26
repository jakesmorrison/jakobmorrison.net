from django.shortcuts import render

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