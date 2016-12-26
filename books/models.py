from django.db import models

# Create your models here.

class Books(models.Model):
    Title = models.CharField(max_length=100, unique=True)
    Lookup = models.CharField(max_length=100, default="x")
    Author = models.CharField(max_length=100, default="x")
    Type = models.CharField(max_length=100, default="x")
    Genre = models.CharField(max_length=100, default="x")
    Date_Start = models.DateField()
    Date_Finish = models.DateField()
    Word_Count = models.IntegerField()
    Unique_Words = models.IntegerField()
    Vocab_Density = models.FloatField()
    Word_List = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self.Title,self.Lookup,self.Author,self.Type,self.Genre,self.Date_Start,self.Date_Finish,self.Word_Count,
                           self.Unique_Words,self.Vocab_Density,self.Word_List)
