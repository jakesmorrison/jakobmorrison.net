from django.shortcuts import render
from .models import TravelStats
import pandas as pd
from collections import Counter, OrderedDict
# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'travel/stats_home.html', context)

# def euro(request):
#     context = {
#     }
#     return render(request, 'travel/stats_home.html', context)
#

def general(request):
    df = pd.DataFrame(list(TravelStats.objects.all().values()))
    temp_dict = Counter(df["city"].tolist())
    city_day_counter = sorted(temp_dict.items(), key=lambda x: x[1])[::-1]

    city_list = [x[0] for x in city_day_counter]
    city_day_count = [x[1] for x in city_day_counter]

    context = {
        "city_list": city_list,
        "city_day_count": city_day_count,
    }
    return render(request, 'travel/general_info.html', context)

def media(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def sleep(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def food(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def transportation(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def other(request):
    context = {}
    return render(request, 'travel/general_info.html', context)