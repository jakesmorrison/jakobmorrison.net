from django.db import models
from picklefield.fields import PickledObjectField
# pip install django-picklefield

# Create your models here.
class Game(models.Model):
    gameId = models.IntegerField(primary_key=True)
    gameStarted = models.BooleanField(default=False)
    gameDeck = PickledObjectField(default = {})
    playerOrder = models.CharField(max_length=100,default='x')
    cardsPlayed = PickledObjectField(default = {})
    def __str__(self):
        return "{} {} {}".format(self.gameId, self.gameStarted, self.playerOrder, self.gameDeck, self.cardsPlayed)

class Player(models.Model):
    playerId = models.IntegerField(primary_key=True)
    gameId = models.ForeignKey('Game')
    playerName = models.CharField(max_length=20,default='random_name')
    card1 = models.CharField(max_length=1, default="-1")
    card2 = models.CharField(max_length=1, default="-1")
    score = models.IntegerField()
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.playerId,self.playerName,self.card1,self.card2,self.score,self.gameId)