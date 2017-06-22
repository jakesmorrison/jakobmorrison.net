from django.contrib import admin

# Register your models here.

class CreditCardModelAdmin(admin.ModelAdmin):
    list_display= "self.cc_id,self.issuer,self.card,self.date_approved,self.bonus_recieved," \
                  "self.bonus,self.min_spend,self.fee,self.line".replace("self.","").split(",")
    search_fields = list_display
from .models import CreditCard
admin.site.register(CreditCard, CreditCardModelAdmin)

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["user_id","name","email"]
    search_fields = list_display
from .models import User
admin.site.register(User,UserModelAdmin)

class IssuedModelAdmin(admin.ModelAdmin):
    list_display = ["issue_id","cc_id","user_id"]
    search_fields = list_display
from .models import Issued
admin.site.register(Issued,IssuedModelAdmin)


class TravelStatsModelAdmin(admin.ModelAdmin):
    list_display = "self.date, self.city, self.country, self.traveling_with, self.wake_time, self.sleep_time, self.naps, self.breakfast_time, self.breakfast_cost, self.breakfast_type, self.lunch_time, self.lunch_cost, self.lunch_type, self.dinner_time, self.dinner_cost, self.dinner_type, self.glasses_of_wine, self.wine_cost, self.cocktail_count, self.cocktail_cost, self.miles_air, self.miles_train, self.miles_bus, self.miles_car, self.miles_walk, self.housing_cost, self.housing_name, self.housing_type, self.num_sex, self.num_master, self.num_poops, self.hours_read, self.book, self.show, self.hours_tv, self.num_pictures_taken, self.hours_podcast, self.podcast, self.hours_music, self.museums_visited, self.friends_met, self.tour_name, self.tour_cost".replace(" ", "").replace("self.","").split(",")
    search_fields = list_display
from .models import TravelStats
admin.site.register(TravelStats,TravelStatsModelAdmin)