from django.shortcuts import render

# Create your views here

def index(request):
    context = {}
    return render(request, 'resume/index.html', context)

def developer(request):
    context = {}
    return render(request, 'resume/developer.html', context)


def applications(request):
    context = {}
    return render(request, 'resume/applications.html', context)
