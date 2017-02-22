from django.db import models

# Create your models here.

class Books(models.Model):
    Title = models.CharField(max_length=100, default='x')
    Lookup = models.CharField(max_length=100, default="x")
    Author = models.CharField(max_length=100, default="x")
    Type = models.CharField(max_length=100, default="x")
    Genre = models.CharField(max_length=100, default="x")
    Date_Start = models.DateField()
    Date_Finish = models.DateField()
    Word_Count = models.IntegerField(default=0)
    Sentence_Count = models.IntegerField(default=0)
    Word_Per_Sentence = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    Unique_Words = models.IntegerField(default=0)
    Average_Unique_Word_Length = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    Vocab_Density = models.FloatField(default=0)
    Unique_Word_list = models.TextField(null=True)
    Occurance_Dict = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self.Title,self.Lookup,self.Author,self.Type,self.Genre,self.Date_Start,self.Date_Finish,self.Word_Count,
                       self.Unique_Words,self.Vocab_Density,self.Unique_Word_list,self.Occurance_Dict)
