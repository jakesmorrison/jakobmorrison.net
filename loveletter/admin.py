from django.contrib import admin

# Register your models here.
class GameModelAdmin(admin.ModelAdmin):
    list_display=['gameId','playerOrder','gameDeck','cardsPlayed']
    search_fields = list_display
from .models import Game
admin.site.register(Game, GameModelAdmin)

class PlayerModelAdmin(admin.ModelAdmin):
    list_display=['playerId','playerId', 'card1', 'card2', 'score', 'gameId']
    search_fields = list_display
from .models import Player
admin.site.register(Player, PlayerModelAdmin)
