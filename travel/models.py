from django.db import models

# Create your models here.

class CreditCard(models.Model):
    issuer = models.CharField(max_length=100, default='x')
    card = models.CharField(max_length=100, default='x')
    date_approved = models.DateField()
    bonus_recieved = models.DateField()
    bonus = models.IntegerField(default=0)
    min_spend = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    line = models.IntegerField(default=0)
    def __str__(self):
        return "{} {} {} {} {} {}".format()
