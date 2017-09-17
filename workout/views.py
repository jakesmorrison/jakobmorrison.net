from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.http import JsonResponse
import json

from .models import Workouts, Stats


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


from datetime import datetime
from pytz import timezone
def add_to_db(request):
    params = request.GET

    type = params["type"]
    exercise = params["exercise"]
    reps = params["reps"]
    weight = params["weight"]
    set = params["set"]


    fmt = "%Y-%m-%d"
    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    # Convert to US/Pacific time zone
    now_pacific = now_utc.astimezone(timezone('US/Mountain'))
    date = now_pacific.strftime(fmt)

    s = Stats(Date=date, Type=type, Exercise=exercise, Reps=int(reps), Weight=int(weight), Set=int(set))
    s.save()

    context = {
    }
    return JsonResponse(json.loads(json.dumps(context)))

