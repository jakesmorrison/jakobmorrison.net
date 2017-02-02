from django.contrib import admin

# Register your models here.
class BooksModelAdmin(admin.ModelAdmin):
    list_display="self.Title,self.Lookup,self.Author,self.Type,self.Genre,self.Date_Start,self.Date_Finish,self.Word_Count," \
                 "self.Unique_Words,self.Vocab_Density".replace(" ","").replace("self.", "").split(",")
    search_fields = list_display
from .models import Books
admin.site.register(Books, BooksModelAdmin)

