from django.shortcuts import render
from django.http import JsonResponse

from .management.functions import LoveLetter


import json
# Create your views here.
'''
Join game or create game.
'''
def main_window(request):
    gameId = LoveLetter().generate_game_id()
    context = {
        'gameId': gameId
    }
    return render(request,'loveletter/main_window.html',context)
    # return render_to_response('loveletter/main_window.html', context, context_instance=RequestContext(request))


def init_game(request):
    params = request.GET
    name = params["name"]
    gameId = params["gameId"]
    LoveLetter().new_game(gameId,name)
    context={
        'name': name,
        'gameId': gameId
    }
    return JsonResponse(json.loads(json.dumps(context)))

def join_game(request):
    params = request.GET
    name = params["name"]
    gameId = params["gameId"]
    LoveLetter().add_player_from_join_game(gameId,name)
    context={
        'name': name,
        'gameId': gameId
    }
    return JsonResponse(json.loads(json.dumps(context)))

def play_game(request):
    params = request.GET
    name = params["name"]
    gameId = params["gameId"]
    players = LoveLetter().get_players(gameId)
    leader = players.split(",")[0]

    context={
        'name': name,
        'gameId': gameId,
        'players': players,
        'leader': leader,
    }
    return render(request, 'loveletter/game_window.html', context)

def refresh_status(request):
    params = request.GET
    gameId = params["gameId"]
    name = params["name"]
    gameStarted = LoveLetter().game_started(gameId)

    if gameStarted == False:
        players = LoveLetter().get_players(gameId)
        context = {
            'players': players,
            "gameStarted": gameStarted
        }
    else:
        mycards = LoveLetter().get_current_card(gameId, name)
        card1 = mycards[0]
        card2 = mycards[1]
        players = LoveLetter().get_players(gameId)
        playerNumber = players.split(",").index(name) + 1

        context = {
            'players': players,
            'card1': card1,
            'card2': card2,
            'playedCards': LoveLetter().board_cards(gameId),
            'playerNumber': playerNumber,
            'playerList': players.split(","),
            "gameStarted": gameStarted
        }

    return JsonResponse(json.loads(json.dumps(context)))

def deal(request):
    params = request.GET
    gameId = params["gameId"]
    LoveLetter().deal(gameId)
    context = {}
    return JsonResponse(json.loads(json.dumps(context)))

def get_new_card(request):
    params = request.GET
    gameId = params["gameId"]
    name = params["name"]
    gameStarted = LoveLetter().game_started(gameId)

    cardsLeft = LoveLetter().get_new_card(gameId,name)
    mycards = LoveLetter().get_current_card(gameId, name)
    card1 = mycards[0]
    card2 = mycards[1]
    context = {'players': name,
               'card1': card1,
               'card2': card2,
               'cardsLeft': cardsLeft,
               "gameStarted": gameStarted
               }

    return JsonResponse(json.loads(json.dumps(context)))

def play_card(request):
    params = request.GET
    gameId = params["gameId"]
    name = params["name"]
    cardNumber = params["cardNumber"]

    LoveLetter().play_card(gameId,name,cardNumber)
    mycards = LoveLetter().get_current_card(gameId, name)
    card1 = mycards[0]
    card2 = mycards[1]

    players = LoveLetter().get_players(gameId)
    playerNumber = players.split(",").index(name) + 1

    context = {
            'players': name,
            'card1': card1,
            'card2': card2,
            'playedCards': LoveLetter().board_cards(gameId),
            'playerNumber': playerNumber,
            'playerList': players.split(",")
            }
    return JsonResponse(json.loads(json.dumps(context)))

