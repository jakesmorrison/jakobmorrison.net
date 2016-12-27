from django.contrib import admin
# Register your models here.

from django.contrib import admin

# Register your models here.

class WordsModelAdmin(admin.ModelAdmin):
    list_display=['word','type','definition']
    search_fields = list_display
from .models import Words
admin.site.register(Words, WordsModelAdmin)
