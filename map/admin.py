from django.contrib import admin

# Register your models here.

class MapModelAdmin(admin.ModelAdmin):
    list_display = "index,address,label,lat,long".split(",")
    search_fields = list_display
from .models import Map
admin.site.register(Map,MapModelAdmin)
