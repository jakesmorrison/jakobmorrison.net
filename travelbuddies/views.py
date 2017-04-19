from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.

@login_required
def home(request):
    context = {}
    return render(request, 'travelbuddies/home.html', context)

def log(request):
    username = request.POST['logged_user']
    password = request.POST['logged_password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        context = {}
        return render(request, "game/invalid_user.html", context)

def signup(request):
    username = request.POST['new_user']
    password = request.POST['new_password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    return HttpResponseRedirect("/")