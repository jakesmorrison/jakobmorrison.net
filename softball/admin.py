from django.contrib import admin

# Register your models here.
class StatsModelAdmin(admin.ModelAdmin):
    list_display="self.season,self.date,self.player,self.games,self.pa,self.ab,self.bb,self.so,self.hidp," \
                 "self.cs,self.dbo,self.sb,self.h,self.firstb,self.secondb,self.thirdb,self.fourthb," \
                 "self.hr,self.r,self.rbi".replace(" ","").replace("self.", "").split(",")
    search_fields = list_display
from .models import Stats
admin.site.register(Stats, StatsModelAdmin)

