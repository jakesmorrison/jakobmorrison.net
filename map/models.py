from django.db import models

# Create your models here.

class Map(models.Model):
    index = models.IntegerField()
    address = models.CharField(max_length=500)
    label = models.CharField(max_length=500)
    lat = models.FloatField()
    long = models.FloatField()
    def __str__(self):
        return "{} {} {} {} {}".format(self.index,self.address,self.label,self.lat,self.long)