from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=25, unique=True)
    type = models.CharField(max_length=25)
    definition = models.CharField(max_length=1000)
    frequency = models.IntegerField(default=0)
    def __str__(self):
        return "{}".format(self.word,self.type,self.definition,self.frequency)