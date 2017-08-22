from django.shortcuts import render
from .models import TravelStats
import pandas as pd
from collections import Counter, OrderedDict
import datetime
import numpy as np
from .management import methods

# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'travel/stats_home.html', context)

def general(request):
    df = pd.DataFrame(list(TravelStats.objects.all().values()))
    df = df[df["country"]!="United States"].reset_index()

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
    df = df[df["country"]!="United States"].reset_index()

    wake = df["wake_time"].tolist()
    sleep = df["sleep_time"].tolist()
    wake = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in wake]
    sleep = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in sleep]

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
        radial_wake_list.append({'type':'line','name':'Occurrences','data':[0,val],'pointStart':0,'pointInterval':key,'color':'magenta','lineWidth': 5,'marker':{'symbol':'circle'}})

    sleep_dict = Counter(sleep_list)
    radial_sleep_list = []
    for key,val in sleep_dict.items():
        radial_sleep_list.append({'type':'line','name':'Occurrences','data':[0,val],'pointStart':0,'pointInterval':key,'color':'cyan','lineWidth': 5,'marker':{'symbol':'circle'}})


    # average_minutes_wake = methods.Travel_Methods.convert_to_minutes(wake)
    # average_time_wake = methods.Travel_Methods.convert_to_hours(average_minutes_wake)
    #
    # wake_solo = df[df["traveling_with"]=="Solo"]["wake_time"].tolist()
    # wake_solo = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in wake_solo]
    # average_minutes_wake_solo = methods.Travel_Methods.convert_to_minutes(wake_solo)
    # average_time_wake_solo = methods.Travel_Methods.convert_to_hours(average_minutes_wake_solo)
    #
    # wake_joie = df[df["traveling_with"]=="Joie"]["wake_time"].tolist()
    # wake_joie = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in wake_joie]
    # average_minutes_wake_joie = methods.Travel_Methods.convert_to_minutes(wake_joie)
    # average_time_wake_joie = methods.Travel_Methods.convert_to_hours(average_minutes_wake_joie)
    #
    # wake_mom = df[df["traveling_with"]=="Mom"]["wake_time"].tolist()
    # wake_mom = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in wake_mom]
    # average_minutes_wake_mom = methods.Travel_Methods.convert_to_minutes(wake_mom)
    # average_time_wake_mom = methods.Travel_Methods.convert_to_hours(average_minutes_wake_mom)
    #
    #
    # sleep_all = df["sleep_time"].tolist()
    # sleep_all = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in sleep_all]
    #
    # average_minutes_bed = methods.Travel_Methods.convert_to_minutes(sleep_all)
    # average_time_bed = methods.Travel_Methods.convert_to_hours(average_minutes_bed)
    #
    # bed_solo = df[df["traveling_with"]=="Solo"]["sleep_time"].tolist()
    # bed_solo = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in bed_solo]
    # average_minutes_bed_solo = methods.Travel_Methods.convert_to_minutes(bed_solo)
    # average_time_bed_solo = methods.Travel_Methods.convert_to_hours(average_minutes_bed_solo)
    #
    # bed_joie = df[df["traveling_with"]=="Joie"]["sleep_time"].tolist()
    # bed_joie = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in bed_joie]
    # average_minutes_bed_joie = methods.Travel_Methods.convert_to_minutes(bed_joie)
    # average_time_bed_joie = methods.Travel_Methods.convert_to_hours(average_minutes_bed_joie)
    #
    # bed_mom = df[df["traveling_with"]=="Mom"]["sleep_time"].tolist()
    # bed_mom = [float("%.2f" %(int(str(x).split(":")[0])+int(str(x).split(":")[1])/100)) for x in bed_mom]
    # average_minutes_bed_mom = methods.Travel_Methods.convert_to_minutes(bed_mom)
    # average_time_bed_mom = methods.Travel_Methods.convert_to_hours(average_minutes_bed_mom)


    cities = Counter(df["city"].tolist())
    city_day_counter = sorted(cities.items(), key=lambda x: x[1])[::-1]
    city_list = df["city"].tolist()
    new_city_list = []
    for x in city_list:
        if x in new_city_list:
            pass
        else:
            new_city_list.append(x)
    city_list = new_city_list


    #Accommodation Cost vs. Days Stayed vs. City
    df["housing_cost"] = df["housing_cost"].apply(lambda x: int(x))

    df_cost = df.groupby(['housing_type', 'city'])['housing_cost'].sum().reset_index()
    df_acc = df.groupby(['housing_type','city'])['housing_cost'].count().reset_index()


    acc_data = []
    acc_data_average = []
    for index, row in df_cost.iterrows():
        city = row["city"]
        df_acc_city = df_acc[df_acc['city']==city]
        days_stayed = df_acc_city[df_acc_city['housing_type']==row["housing_type"]]['housing_cost'].tolist()[0]

        city_index = city_list.index(city)
        color = "#7a7a7a"
        if row["housing_type"] == 'Hotel':color='#ff4d4d'
        elif row["housing_type"] == 'Airbnb':color='#ff4dff'
        elif row["housing_type"] == 'Hostel':color='#4dff4d'

        avg_cost = float("%.2f" % (float(row['housing_cost'])/int(days_stayed)))
        foo = {'x':city_index,'y':float(row['housing_cost']),'z':int(days_stayed),'name':row["housing_type"],'city':row['city'],'color':color,'avg':avg_cost}
        foo1 = {'x':city_index,'y':avg_cost,'z':int(days_stayed),'name':row["housing_type"],'city':row['city'],'color':color,'total':float(row['housing_cost']),'nights':int(days_stayed)}
        acc_data.append(foo)
        acc_data_average.append(foo1)



    # I didnt actually pay money for the hotels so I am not including them in this data.
    # df_per_person = df[df["housing_type"]!="Hotel"]
    df_per_person = df
    average_by_person = df_per_person.groupby(["traveling_with"]).mean()["housing_cost"].reset_index()
    # average_by_person_html = average_by_person.to_html()
    housing_cost_solo = (average_by_person[average_by_person["traveling_with"]=="Solo"]["housing_cost"].tolist()[0])
    housing_cost_joie = (average_by_person[average_by_person["traveling_with"]=="Joie"]["housing_cost"].tolist()[0])
    housing_cost_mom = (average_by_person[average_by_person["traveling_with"]=="Mom"]["housing_cost"].tolist()[0])

    country_list = df["country"].tolist()
    new_country_list = []
    for x in country_list:
        if x in new_country_list:
            pass
        else:
            new_country_list.append(x)
    country_list=new_country_list
    df_cost_country= df.groupby(["country"]).describe()["housing_cost"].reset_index()

    box_data = []
    for x in country_list:
        foo = df_cost_country[df_cost_country["country"]==x]
        temp = [foo[foo["level_1"]=="min"]["housing_cost"].tolist()[0],foo[foo["level_1"] == "25%"]["housing_cost"].tolist()[0],foo[foo["level_1"] == "50%"]["housing_cost"].tolist()[0],foo[foo["level_1"] == "75%"]["housing_cost"].tolist()[0],foo[foo["level_1"] == "max"]["housing_cost"].tolist()[0]]
        box_data.append(temp)


    context = {
        'wake': wake,
        'sleep': sleep,
        'radial_wake': radial_wake_list,
        'radial_sleep': radial_sleep_list,
        # 'average_time_wake': average_time_wake,
        # 'average_time_wake_solo': average_time_wake_solo,
        # 'average_time_wake_joie': average_time_wake_joie,
        # 'average_time_wake_mom': average_time_wake_mom,
        # 'average_time_bed': average_time_bed,
        # 'average_time_bed_solo': average_time_bed_solo,
        # 'average_time_bed_joie': average_time_bed_joie,
        # 'average_time_bed_mom': average_time_bed_mom,
        'city_list':city_list,
        'acc_data': acc_data,
        'acc_data_avg': acc_data_average,
        'average_cost_solo':"%.2f" % housing_cost_solo,
        'average_cost_joie':"%.2f" % housing_cost_joie,
        'average_cost_mom':"%.2f" % housing_cost_mom,
        'country_list': country_list,
        'box_data':box_data,
        'total_cost': "%.2f" % sum(df["housing_cost"].tolist()),
    }
    return render(request, 'travel/sleep_info.html', context)

def food(request):
    # [{
    #     name: 'John',
    #     data: [5, 3, 4, 7, 2]
    # }, {
    #     name: 'Jane',
    #     data: [2, 2, 3, 2, 1]
    # }, {
    #     name: 'Joe',
    #     data: [3, 4, 4, 2, 5]
    # }]

    df = pd.DataFrame(list(TravelStats.objects.all().values()))
    df = df[df["country"]!="United States"].reset_index()

    city_list = df["city"].tolist()
    new_city_list = []
    for x in city_list:
        if x in new_city_list:
            pass
        else:
            new_city_list.append(x)
    city_list = new_city_list

    df["lunch_cost"] = df["lunch_cost"] .apply(lambda x: float(x))
    df["breakfast_cost"] = df["breakfast_cost"] .apply(lambda x: float(x))
    df["dinner_cost"] = df["dinner_cost"] .apply(lambda x: float(x))
    df_food_group_sum = df.groupby(["city", "country"]).sum().reset_index()
    df_food_group_avg = df.groupby(["city", "country"]).mean().reset_index()

    food_sum_city_dinner = []
    food_sum_city_lunch = []
    food_sum_city_breakfast = []
    food_avg_city_dinner = []
    food_avg_city_lunch = []
    food_avg_city_breakfast = []

    for x in city_list:
        city_data = df_food_group_avg[df_food_group_avg["city"]==x]
        city_data_sum = df_food_group_sum[df_food_group_sum["city"]==x]

        if city_data["country"].tolist()[0] in ["Italy", "Spain", "Portugal"]:
            food_avg_city_dinner.append(float("%.2f" %(city_data["dinner_cost"].tolist()[0]/2)))
            food_avg_city_lunch.append(float("%.2f" %(city_data["lunch_cost"].tolist()[0]/2)))
            food_avg_city_breakfast.append(float("%.2f" %(city_data["breakfast_cost"].tolist()[0]/2)))

            food_sum_city_dinner.append(float("%.2f" %(city_data_sum["dinner_cost"].tolist()[0]/2)))
            food_sum_city_lunch.append(float("%.2f" %(city_data_sum["lunch_cost"].tolist()[0]/2)))
            food_sum_city_breakfast.append(float("%.2f" %(city_data_sum["breakfast_cost"].tolist()[0]/2)))

        else:
            food_avg_city_dinner.append(float("%.2f" %(city_data["dinner_cost"].tolist()[0])))
            food_avg_city_lunch.append(float("%.2f" %(city_data["lunch_cost"].tolist()[0])))
            food_avg_city_breakfast.append(float("%.2f" %(city_data["breakfast_cost"].tolist()[0])))

            food_sum_city_dinner.append(float("%.2f" %(city_data_sum["dinner_cost"].tolist()[0])))
            food_sum_city_lunch.append(float("%.2f" %(city_data_sum["lunch_cost"].tolist()[0])))
            food_sum_city_breakfast.append(float("%.2f" %(city_data_sum["breakfast_cost"].tolist()[0])))


    food_avg_city_data = [{'name': 'Breakfast', 'data': food_avg_city_breakfast},
                          {'name': 'Lunch', 'data': food_avg_city_lunch},
                           {'name': 'Dinner', 'data': food_avg_city_dinner}]

    context = {
        'food_avg_city_data':food_avg_city_data,
        'cities': city_list,
        'total_food_cost': "%.2f" % (sum(food_sum_city_dinner)+sum(food_sum_city_lunch)+sum(food_sum_city_breakfast)),
        'total_breakfast_cost': "%.2f" % sum(food_sum_city_breakfast),
        'total_lunch_cost': "%.2f" % sum(food_sum_city_lunch),
        'total_dinner_cost': "%.2f" % sum(food_sum_city_dinner),
    }
    return render(request, 'travel/gelato_info.html', context)

def transportation(request):
    context = {}
    return render(request, 'travel/general_info.html', context)

def other(request):
    context = {}
    return render(request, 'travel/general_info.html', context)