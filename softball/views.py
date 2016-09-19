from django.shortcuts import render
from .models import Stats
import pandas as pd
import re
from .management import methods

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

    df_plot = methods.Softball_Methods.plot_data(df)
    print(df_plot)

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


    context = {
        'table': new_table
    }
    return(render(request, 'softball/index.html',context))

def index_updates(request):
    # db_attri = Attribute.objects.all().filter(design_id=dbase, mfg_workweek__in=([str(x) for x in cfg.ALL_WORKWEEKS]))
    pass