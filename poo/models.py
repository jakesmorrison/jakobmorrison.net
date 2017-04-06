from django.db import models

# Create your models here.

class Poo(models.Model):
    name = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    movement = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    def __str__(self):
        return "{} {} {} {} {}".format(self.name,self.time,self.date,self.movement,self.type)