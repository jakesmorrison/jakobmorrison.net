from django.db import models

# Create your models here.

class CreditCard(models.Model):
    cc_id = models.CharField(primary_key=True, max_length=100)
    issuer = models.CharField(max_length=100, default='x')
    card = models.CharField(max_length=100, default='x')
    date_approved = models.DateField()
    bonus_recieved = models.DateField()
    bonus = models.IntegerField(default=0)
    min_spend = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    line = models.IntegerField(default=0)
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.cc_id,self.issuer,self.card,self.date_approved,self.bonus_recieved,
                                                   self.bonus,self.min_spend,self.fee,self.line)

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, default='x')
    email = models.CharField(max_length=100, default='x')
    def __str__(self):
        return "{} {} {}".format(self.user_id,self.name,self.email)


class Issued(models.Model):
    issue_id = models.CharField(primary_key=True, max_length=100)
    cc_id = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {} {}".format(self.issue_id,self.cc_id,self.user_id)

class TravelStats(models.Model):
    date = models.DateField()
    city =  models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    traveling_with = models.CharField(max_length=100)

    wake_time = models.TimeField()
    sleep_time = models.TimeField()
    naps = models.IntegerField(default=0)

    breakfast_time = models.TimeField()
    breakfast_cost = models.DecimalField(max_digits=5, decimal_places=2)
    breakfast_type = models.CharField(max_length=100)

    lunch_time = models.TimeField()
    lunch_cost = models.DecimalField(max_digits=5, decimal_places=2)
    lunch_type = models.CharField(max_length=100)

    dinner_time = models.TimeField()
    dinner_cost = models.DecimalField(max_digits=5, decimal_places=2)
    dinner_type = models.CharField(max_length=100)

    glasses_of_wine = models.IntegerField(default=0)
    wine_cost = models.DecimalField(max_digits=5, decimal_places=2)
    cocktail_count = models.IntegerField(default=0)
    cocktail_cost = models.DecimalField(max_digits=5, decimal_places=2)

    miles_air = models.IntegerField(default=0)
    miles_train = models.IntegerField(default=0)
    miles_car = models.IntegerField(default=0)
    miles_bus = models.IntegerField(default=0)
    miles_walk = models.DecimalField(max_digits=5, decimal_places=2)

    housing_cost = models.DecimalField(max_digits=5, decimal_places=2)
    housing_name = models.CharField(max_length=100)
    housing_type = models.CharField(max_length=100)

    num_sex = models.IntegerField(default=0)
    num_master = models.IntegerField(default=0)

    num_poops = models.IntegerField(default=0)

    hours_read = models.DecimalField(max_digits=5, decimal_places=2)
    book = models.CharField(max_length=100)

    hours_tv = models.DecimalField(max_digits=5, decimal_places=2)
    show = models.CharField(max_length=100)

    hours_podcast = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    podcast = models.CharField(max_length=100, default="")

    hours_music = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    museums_visited = models.IntegerField(default=0)

    friends_met = models.IntegerField(default=0)

    tour_name = models.CharField(max_length=100, default="")
    tour_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    num_pictures_taken = models.IntegerField(default=0)

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(
            self.date, self.city, self.country, self.traveling_with, self.wake_time, self.sleep_time, self.naps, self.breakfast_time, self.breakfast_cost,
            self.breakfast_type, self.lunch_time, self.lunch_cost, self.lunch_type, self.dinner_time, self.dinner_cost, self.dinner_type, self.glasses_of_wine,
            self.wine_cost, self.cocktail_count, self.cocktail_cost, self.miles_air, self.miles_train, self.miles_bus, self.miles_car, self.miles_walk,
            self.housing_cost, self.housing_name, self.housing_type, self.num_sex, self.num_master, self.num_poops, self.hours_read, self.book,
            self.show, self.hours_tv, self.num_pictures_taken, self.hours_podcast, self.podcast, self.hours_music, self.museums_visited, self.friends_met,
            self.tour_name, self.tour_cost)

