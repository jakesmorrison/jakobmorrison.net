from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.

class Stats(models.Model):
    season = models.CharField(max_length=100, default='x')
    date = models.DateField()
    player = models.CharField(max_length=100, default='x')
    games = models.IntegerField(default=0)
    pa = models.IntegerField(default=0)
    ab = models.IntegerField(default=0)
    bb = models.IntegerField(default=0)
    so = models.IntegerField(default=0)
    hidp = models.IntegerField(default=0)
    cs = models.IntegerField(default=0)
    dbo = models.IntegerField(default=0)
    sb = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    firstb = models.IntegerField(default=0)
    secondb = models.IntegerField(default=0)
    thirdb = models.IntegerField(default=0)
    fourthb = models.IntegerField(default=0)
    hr = models.IntegerField(default=0)
    r = models.IntegerField(default=0)
    rbi = models.IntegerField(default=0)
    def __str__(self):
        return "{}".format(self.season,self.date,self.player,self.games,self.pa,self.ab,self.bb,self.so,self.hidp,
                           self.cs,self.dbo,self.sb,self.h,self.firstb,self.secondb,self.thirdb,self.fourthb,
                           self.hr,self.r,self.rbi)


# class Polls(models.Model):
#     question = models.CharField(max_length=1000, default='x')
#     poss = PickledObjectField(default={})
#     def __str__(self):
#         return "{} {}".format(self.question,self.poss)