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
        print(self.cc_id)
        return "{} {} {}".format(self.issue_id,self.cc_id,self.user_id)
