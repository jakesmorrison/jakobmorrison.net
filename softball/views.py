from django.shortcuts import render
from django.http import JsonResponse

from .models import Stats
import pandas as pd
import re
from .management import methods
import json

from .management import config as cfg
cfg = cfg.Config
import time


# Create your views here.
def index(request):
    # Converting db to df
    db_stats = Stats.objects.all().filter(season = cfg.CURRENT_SEASON, player__in = cfg.CURRENT_SEASON_ROSTER)
    df = pd.DataFrame(list(db_stats.values()))
    df =df.drop("id",1)
    df.columns = cfg.COLUMN_NAMES
    df = df[cfg.COLUMN_NAMES_ORDER]


    db_for_sel = Stats.objects.all()
    df_for_sel = pd.DataFrame(list(db_for_sel.values()))
    df_for_sel =df_for_sel.drop("id",1)
    df_for_sel.columns = cfg.COLUMN_NAMES
    df_for_sel = df_for_sel[cfg.COLUMN_NAMES_ORDER]

    df_plot = methods.Softball_Methods.plot_data(df)

    # Getting season stats
    df_season = methods.Softball_Methods.season_stats(df)

    df_table = df_season.to_html(index=False,classes='table table-striped table-bordered table-hover table-responsive" id="table-custom-sort')

    count = 0
    cat_list = []
    new_table = ""
    for line in df_table.split("\n"):
        m_th = re.search("<th>", line)
        m_td = re.search("<td>", line)
        m_tr = re.search("<tr>", line)
        if (m_tr):
            count = 0
        elif (m_th):
            cat_list.append(line.replace("<th>","").replace("</th>","").replace(" ",""))
        elif (m_td):
            line = line.replace("<td>","<td class='"+cat_list[count]+"'>")
            count += 1
        new_table = new_table + line+"\n"


    # high charts data
    '''
    array of dictionary objects.
    [{name: "Game1", data[all game 1 ops data]},{}]
    '''
    series = []
    roster = sorted(cfg.CURRENT_SEASON_ROSTER)
    dates = list(sorted(set(df_plot["Date"].tolist())))
    for date in dates:
        df_temp = df_plot[df_plot["Date"] == date]
        df_temp = df_temp.sort(["Player"])
        series.append({"name":str(date),"data":df_temp["OPS"].tolist()})

    context = {
        'table': new_table,
        'current_season': cfg.CURRENT_SEASON,
        'seasons': ["All"]+sorted(list(set(df_for_sel["Season"].tolist()))),
        'players': ["All"] + sorted(list(set(df_for_sel[df_for_sel["Season"] == cfg.CURRENT_SEASON]["Player"].tolist())), ),
        'games': ["All"]+sorted(list(set(df_for_sel[df_for_sel["Season"]==cfg.CURRENT_SEASON]["Date"].apply(lambda x: str(x)).tolist()))),
        'dataType': "OPS",
        'rosterCats': roster,
        'seriesData': series,
    }
    return(render(request, 'softball/index2.html',context))

def index_updates(request):
    params = request.GET
    season = params["season"]
    game = params["game"]
    player = params["player"]

    db_stats = Stats.objects.all()
    df = pd.DataFrame(list(db_stats.values()))
    df =df.drop("id",1)
    df.columns = cfg.COLUMN_NAMES
    df = df[cfg.COLUMN_NAMES_ORDER]
    df_self = df

    if season != "All":
        df = df[df["Season"]==season]
    if game != "All":
        df["Date"] = df["Date"].apply(lambda x: str(x))
        df = df[df["Date"] == game]
    if player != "All":
        df = df[df["Player"]==player]

    if season == "All" and game == "All" and player=="All":
        df_season = df.drop("Season", 1)
        df_season = df_season.groupby(["Player"]).sum().reset_index()
        df_season = df_season[df_season["Games"]>5]
        df_season = methods.Softball_Methods.stats_calc(df_season)
    elif game != "All":
        df_season = methods.Softball_Methods.stats_calc(df)
        df_season = df_season[df_season["Games"]==1]
    elif player != "All":
        df_season = methods.Softball_Methods.game_stats(df)
    else:
        df_season = methods.Softball_Methods.season_stats(df)


    df_table = df_season.to_html(index=False,classes='table table-striped table-bordered table-hover table-responsive" id="table-custom-sort')
    count = 0
    cat_list = []
    new_table = ""
    for line in df_table.split("\n"):
        m_th = re.search("<th>", line)
        m_td = re.search("<td>", line)
        m_tr = re.search("<tr>", line)
        if (m_tr):
            count = 0
        elif (m_th):
            cat_list.append(line.replace("<th>","").replace("</th>","").replace(" ",""))
        elif (m_td):
            line = line.replace("<td>","<td class='"+cat_list[count]+"'>")
            count += 1
        new_table = new_table + line+"\n"

    context = {
        "table": new_table,
        'seasons': ["All"] + sorted(list(set(df_self["Season"].tolist()))),
        'players': ["All"] + sorted(list(set(df_self[df_self["Season"] == season]["Player"].tolist()))),
        'games': ["All"] + sorted(list(set(df_self[df_self["Season"] == season]["Date"].apply(lambda x: str(x)).tolist()))),
        'current_season': season,
        'current_players': player,
        'current_game': game,
    }
    return JsonResponse(json.loads(json.dumps(context)))

def change_season(request):
    params = request.GET
    season = params["season"]

    db_stats = Stats.objects.all()
    df = pd.DataFrame(list(db_stats.values()))
    df =df.drop("id",1)
    df.columns = cfg.COLUMN_NAMES
    df = df[cfg.COLUMN_NAMES_ORDER]
    df_self = df

    context = {
        "game_list": ["All"] + sorted(list(set(df_self[df_self["Season"] == season]["Date"].apply(lambda x: str(x)).tolist())))
    }
    return JsonResponse(json.loads(json.dumps(context)))
