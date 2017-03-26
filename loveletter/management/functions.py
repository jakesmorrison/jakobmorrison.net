import numpy as np
import random
from ..models import Game, Player
from .config import Config

class LoveLetter(object):
    def __init__(self):
        pass
    def generate_game_id(self):
        gameId = "".join([str(x) for x in np.random.randint(0, 10, size=6)])
        if self.check_game_id(gameId) == False:
            return gameId
        else:
            self.generate_game_id()

    def check_game_id(self, gameId):
        gameIds = [x['gameId'] for x in Game.objects.values()]
        if gameId in gameIds:
            return True
        else:
            return False

    def generate_player_id(self):
        playerId = "".join([str(x) for x in np.random.randint(0, 10, size=6)])
        if self.check_player_id(playerId) == False:
            return playerId
        else:
            self.generate_player_id()

    def check_player_id(self, playerId):
        playerIds = [x['playerId'] for x in Player.objects.values()]
        if playerId in playerIds:
            return True
        else:
            return False

    def card_deck(self):
        cardDeck = {
            'x': 1,
            '0': 1,
            '1': 5,
            '2': 2,
            '3': 2,
            '4': 2,
            '5': 2,
            '6': 1,
            '7': 1,
            '8': 1,
            '9': 1,
        }
        return cardDeck

    def new_game(self,gameId, name):
        obj = Game()
        obj.gameId = gameId
        obj.gameDeck = self.card_deck()
        obj.playerOrder = name
        obj.save()
        self.add_player_from_new_game(Game.objects.get(gameId=gameId), name)

    """
    New game. Add player.
    """
    def add_player_from_new_game(self,gameId, name):
        p = Player(
            playerId = self.generate_player_id(),
            gameId = gameId,
            playerName = name,
            card1 = "-1",
            card2="-1",
            score = 0,
        )
        p.save()

    """
    Join game. Add player. Add player order to Game model.
    """
    def add_player_from_join_game(self,gameId, name):
        p = Player(
            playerId = self.generate_player_id(),
            gameId = Game.objects.get(gameId=gameId),
            playerName = name,
            card1 = "-1",
            card2="-1",
            score = 0,
        )
        p.save()
        obj = Game.objects.get(gameId=gameId)
        playerOrder = obj.playerOrder+","+name
        obj.playerOrder = playerOrder
        obj.save()

    def get_players(self,gameId):
        obj = Game.objects.get(gameId=gameId)
        players = obj.playerOrder
        return players

    def deal(self,gameId):
        obj = Game.objects.get(gameId=gameId)
        players = obj.playerOrder.split(",")
        deck = obj.gameDeck
        possibleOptions = []
        for key,val in deck.items():
            possibleOptions = possibleOptions + [key]*val
        random.shuffle(possibleOptions)

        hiddenCard = possibleOptions.pop()

        for player in players:
            playerObj = Player.objects.get(gameId = obj, playerName = player)
            playerObj.card1 = possibleOptions.pop()
            playerObj.save()
        newDict = {}
        for x in possibleOptions:
            if x in newDict:
                newDict[x] = newDict[x] + 1
            else:
                newDict[x] = 1
        obj.gameDeck = newDict
        obj.gameStarted = True
        obj.save()

    def game_started(self, gameId):
        obj = Game.objects.get(gameId=gameId)
        if obj.gameStarted == False:
            return False
        else:
            return True
    def get_current_card (self, gameId, name):
        obj = Game.objects.get(gameId=gameId)
        playerObj = Player.objects.get(gameId=obj, playerName=name)
        card1 = playerObj.card1
        card2 = playerObj.card2
        current_card_names = []
        if card1 != '-1':
            current_card_names.append(Config().card_lookup[card1])
        else:
            current_card_names.append("na")

        if card2 != '-1':
            current_card_names.append(Config().card_lookup[card2])
        else:
            current_card_names.append("na")

        return current_card_names

    def get_new_card(self, gameId, name):
        obj = Game.objects.get(gameId=gameId)
        deck = obj.gameDeck
        possibleOptions = []
        for key, val in deck.items():
            possibleOptions = possibleOptions + [key] * val
        random.shuffle(possibleOptions)

        playerObj = Player.objects.get(gameId=obj, playerName=name)
        if playerObj.card1 == '-1':
            playerObj.card1 = str(possibleOptions.pop())
            playerObj.save()
        elif playerObj.card2 == '-1':
            playerObj.card2 = str(possibleOptions.pop())
            playerObj.save()
        newDict = {}
        for x in possibleOptions:
            if x in newDict:
                newDict[x] = newDict[x] + 1
            else:
                newDict[x] = 1
        obj.gameDeck = newDict
        obj.gameStarted = True
        obj.save()
        return len(possibleOptions)

    def play_card(self, gameId, name, cardNum):
        obj = Game.objects.get(gameId=gameId)
        playerObj = Player.objects.get(gameId=obj, playerName=name)
        card = ""
        if cardNum == "1":
            card = playerObj.card1
            playerObj.card1 = "-1"
            playerObj.save()

        elif cardNum == "2":
            card = playerObj.card2
            playerObj.card2 = "-1"
            playerObj.save()

        cardsPlayed = obj.cardsPlayed
        if name in cardsPlayed:
            cardsPlayed[name] = cardsPlayed[name] + [card]
        else:
            cardsPlayed[name] = [card]
        obj.cardsPlayed = cardsPlayed
        obj.save()

    def board_cards(self, gameId):
        return Game.objects.get(gameId=gameId).cardsPlayed




