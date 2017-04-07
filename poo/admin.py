from django.contrib import admin
# Register your models here.

class PooModelAdmin(admin.ModelAdmin):
    list_display = "name,location,time,date,movement,type".split(",")
    search_fields = list_display
from .models import Poo
admin.site.register(Poo,PooModelAdmin)
