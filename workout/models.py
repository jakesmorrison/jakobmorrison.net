from django.db import models

# Create your models here.

class Workouts(models.Model):
    Type = models.CharField(max_length=100, default='x')
    Exercise = models.CharField(max_length=100, default="x")
    def __str__(self):
        return "{}".format(self.Type, self.Exercise)


class Stats(models.Model):
    Date = models.DateField()
    Reps = models.IntegerField(default=0)
    Set = models.IntegerField(default=0)
    Weight = models.IntegerField(default=0)
    Type = models.CharField(max_length=100, default='x')
    Exercise = models.CharField(max_length=100, default="x")
    def __str__(self):
        return "{}".format(self.Date, self.Reps,self.Set, self.Weight, self.Type, self.Exercise)
