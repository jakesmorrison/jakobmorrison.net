from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.http import JsonResponse
import json

from .models import Workouts


# Create your views here.
@login_required
def home(request):

    type = []
    for x in Workouts.objects.all().values():
        if x['Type'] in type:
            pass
        else:
            type.append((x['Type']))

    context = {
        'type' : type
    }
    return render(request,"workout/home.html",context)

def log(request):
    username = request.POST['logged_user']
    password = request.POST['logged_password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/workout")
    else:
        context = {}
        return render(request, "workout/invalid_user.html", context)

def signup(request):
    username = request.POST['new_user']
    password = request.POST['new_password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    return HttpResponseRedirect("/workout")

def change_type(request):
    params = request.GET
    type = params["type"]

    exercise = []
    for x in Workouts.objects.all().values():
        if x["Type"] == type:
            exercise.append(x["Exercise"])

    context = {
        'exercise': exercise,
    }
    return JsonResponse(json.loads(json.dumps(context)))


