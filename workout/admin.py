from django.contrib import admin

# Register your models here.

class WorkoutsModelAdmin(admin.ModelAdmin):
    list_display = ['Type', 'Exercise']
    search_fields = list_display
from .models import Workouts
admin.site.register(Workouts, WorkoutsModelAdmin)


class StatsModelAdmin(admin.ModelAdmin):
    list_display = ['Date', 'Reps', 'Set','Weight', 'Type', 'Exercise']
    search_fields = list_display
from .models import Stats
admin.site.register(Stats, StatsModelAdmin)
