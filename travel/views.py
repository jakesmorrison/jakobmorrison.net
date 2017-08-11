from django.shortcuts import render
from .models import TravelStats
import pandas as pd
from collections import Counter, OrderedDict
import datetime
# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'travel/stats_home.html', context)

def general(request):
    df = pd.DataFrame(list(TravelStats.objects.all().values()))
    temp_dict = Counter(df["city"].tolist())
    city_day_counter = sorted(temp_dict.items(), key=lambda x: x[1])[::-1]

    city_list = [x[0] for x in city_day_counter]
    city_day_count = [x[1] for x in city_day_counter]

    country_list = df["country"].tolist()
    total_days = len(country_list)
    country_dict = Counter(country_list)

    country_pie = []
    for x in sorted(set(country_list), key=lambda x: country_list.index(x)):
        country_pie.append({'name':x, 'y':int(country_dict[x])})


    city_date = []
    city = ""
    counter = 0
    init_start = ""
    for index, row in df.iterrows():
        #init
        if index == 0:
            city = row["city"]
            counter += 1
            init_start = int(datetime.datetime.strptime(str(row["date"]), "%Y-%m-%d").strftime('%s')) * 1000


        elif city == row["city"]:
            counter+=1
        else:
            city_date.append({"name":city,"data":[100]*(counter+1),'pointStart': init_start, "pointInterval": 24 * 3600 * 1000})
            city = row["city"]
            counter = 1
            init_start = int(datetime.datetime.strptime(str(row["date"]), "%Y-%m-%d").strftime('%s')) * 1000

    #add in last piece
    city_date.append({"name":city,"data":[100]*(counter+1),'pointStart': init_start, "pointInterval": 24 * 3600 * 1000})

    # df_points = pd.read_csv("travel/static/travel/csv/credit_card_data.csv")


    traveling_with = dict(Counter(df["traveling_with"].tolist()))
    other_count = 0
    for key,val in traveling_with.items():
        if key == "Joie" or key== "Solo" or key== "Mom":
            pass
        else:
            other_count+=val
    traveling_with["Other"] = other_count


    context = {
        "city_list": city_list,
        "city_day_count": city_day_count,
        "country_pie": country_pie,
        "day_traveled": total_days,
        "city_date": city_date,
        "traveling_with": traveling_with,
    }
    return render(request, 'travel/general_info.html', context)

def media(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def sleep(request):

    df = pd.DataFrame(list(TravelStats.objects.all().values()))

    wake = df["wake_time"].tolist()
    sleep = df["sleep_time"].tolist()
    wake = [int(str(x).split(":")[0])+int(str(x).split(":")[1])/100 for x in wake]
    sleep = [int(str(x).split(":")[0])+int(str(x).split(":")[1])/100 for x in sleep]

    foo = ""
    for n,x in enumerate(sleep):
        if sleep[n]>=20:
            foo = float(str(int(str(sleep[n]).split(".")[0])-24)+"."+str(sleep[n]).split(".")[1])
            sleep[n] = foo


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
        'wake': wake,
        'sleep': sleep,
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