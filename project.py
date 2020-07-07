#!/usr/bin/env python3
import requests
import webbrowser
import json

## path is = league.games[0].game.home.runs

#input Year
y = input('Enter Year in YYYY format: ')

#input Month
m = input('Enter Month in MM format: ')

#input Day
d = input('Enter Day in DD format: ')

#add date for game and send request
mlb = requests.get(f'https://api.sportradar.us/mlb/trial/v7/en/games/{y}/{m}/{d}/boxscore.json?api_key=x865c2cmk588v462k2gjk42a')

game = mlb.json()

keys = game.keys()

if mlb.status_code == 200:
    print(game)
    print(type(game))
    print(keys)
    print(type(keys))
    print(json.dumps(game, indent=4))


else:
    print('invalid requests')
