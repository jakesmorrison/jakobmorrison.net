from django.shortcuts import render
from datetime import datetime
import pytz
from .models import Poo

# Create your views here.

def index(request):
    context = {
        'loop_times': range(1, 8),
    }
    return render(request,'poo/index.html',context)

def add_data(request):
    params = request.GET
    print(params)
    name = params["name"]
    location = params["location"]
    peeOrpoo = params["peepoo"]
    type = params["type"]
    tz = pytz.timezone('US/Mountain')
    dt = str(datetime.now(tz)).split(" ")
    date = dt[0]
    time = dt[1].split(":")
    time = time[0] +":"+ time[1] +":"+ (time[2]).split(".")[0]

    p = Poo(name=name, loc=location, time=time, date=date, movement=peeOrpoo, type=type)
    p.save()

    context = {}
    return render(request,'poo/index.html',context)