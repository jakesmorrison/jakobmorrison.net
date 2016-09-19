from django.db import models

# Create your models here.

class Stats(models.Model):
    season = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    games = models.IntegerField()
    pa = models.IntegerField()
    ab = models.IntegerField()
    bb = models.IntegerField()
    so = models.IntegerField()
    hidp = models.IntegerField()
    cs = models.IntegerField()
    dbo = models.IntegerField()
    sb = models.IntegerField()
    h = models.IntegerField()
    firstb = models.IntegerField()
    secondb = models.IntegerField()
    thirdb = models.IntegerField()
    fourthb = models.IntegerField()
    hr = models.IntegerField()
    r = models.IntegerField()
    rbi = models.IntegerField()
    def __str__(self):
        return "{}".format(self.season,self.date,self.player,self.games,self.pa,self.ab,self.bb,self.so,self.hidp,
                           self.cs,self.dbo,self.sb,self.h,self.firstb,self.secondb,self.thirdb,self.fourthb,
                           self.hr,self.r,self.rbi)

