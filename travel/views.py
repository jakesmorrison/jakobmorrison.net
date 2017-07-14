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

    df = pd.DataFrame(list(TravelStats.objects.all().values()))

    df_city_wake_sleep = df[["city","wake_time","sleep_time"]]
    df_city_wake_sleep["wake_time_hour"] = df_city_wake_sleep["wake_time"].apply(lambda x: int(str(x).split(":")[0]))
    df_city_wake_sleep["wake_time_min"] = df_city_wake_sleep["wake_time"].apply(lambda x: int(str(x).split(":")[1]))
    df_city_wake_sleep["sleep_time_hour"] = df_city_wake_sleep["sleep_time"].apply(lambda x: int(str(x).split(":")[0]))
    df_city_wake_sleep["sleep_time_min"] = df_city_wake_sleep["sleep_time"].apply(lambda x: int(str(x).split(":")[1]))

    df_city_wake_sleep = df_city_wake_sleep.groupby(['city']).mean().reset_index()
    print(df_city_wake_sleep)


    df_city_wake_sleep["sleep_time"] = df_city_wake_sleep["sleep_time"].apply(lambda x: int(str(x).split(":")[1])+int(str(x).split(":")[1])/60)
    df_city_wake_sleep = df_city_wake_sleep.groupby(['city']).mean().reset_index()

    df_city_wake_sleep["wake_time"] = df_city_wake_sleep["wake_time"].apply(lambda x: str(str(x).split(".")[0]) + ":" +str((float(str(x).split(".")[1])*60)/1000).replace(".",""))
    df_city_wake_sleep["sleep_time"] = df_city_wake_sleep["sleep_time"].apply(lambda x: str(str(x).split(".")[0]) + ":" +str((float(str(x).split(".")[1])*60)/1000).replace(".",""))

    city = list(df_city_wake_sleep["city"].tolist())
    wake = list(df_city_wake_sleep["wake_time"].tolist())
    sleep = list(df_city_wake_sleep["sleep_time"].tolist())

    city_wake_sleep = []
    for n,x in enumerate(city):
        city_wake_sleep.append({'city': city[n],'wake':wake[n], 'sleep':sleep[n]})

    # For radial charts
    df_wake_time = df["wake_time"].tolist()
    df_sleep_time = df["sleep_time"].tolist()
    wake_list = []
    sleep_list = []
    for n,x in enumerate(df_wake_time):
        wake_time = (str(x).split(":"))
        if int(wake_time[0]) == 23 and int(wake_time[1])>=30:
            wake_time = 0
        elif int(wake_time[1])>=30:
            wake_time=int(wake_time[0]) + 1
        else:
            wake_time = int(wake_time[0])
        wake_list.append(wake_time)

        sleep_time = (str(df_sleep_time[n]).split(":"))
        if int(sleep_time[0]) == 23 and int(sleep_time[1])>=30:
            sleep_time = 0
        elif int(sleep_time[1])>=30:
            sleep_time=int(sleep_time[0]) + 1
        else:
            sleep_time = int(sleep_time[0])
        sleep_list.append(sleep_time)


    wake_dict = Counter(wake_list)
    radial_wake_list = []
    for key,val in wake_dict.items():
        radial_wake_list.append({'type':'line','name':'Occurrences','data':[0,val],'pointStart':0,'pointInterval':key,'color':'black','marker':{'symbol':'circle'}})

    sleep_dict = Counter(sleep_list)
    radial_sleep_list = []
    for key,val in sleep_dict.items():
        radial_sleep_list.append({'type':'line','name':'Occurrences','data':[0,val],'pointStart':0,'pointInterval':key,'color':'black','marker':{'symbol':'circle'}})

    context = {
        'city_wake_sleep': city_wake_sleep,
        'radial_wake': radial_wake_list,
        'radial_sleep': radial_sleep_list,
    }
    return render(request, 'travel/sleep_info.html', context)

def food(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def transportation(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def other(request):
    context = {}
    return render(request, 'travel/general_info.html', context)