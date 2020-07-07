import requests

y = "2019"
m = "09"
d = "01"

x = requests.get("https://api.sportradar.us/mlb/trial/v7/en/games/2019/09/01/boxscore.json?api_key=x865c2cmk588v462k2gjk42a")


x = x.json()

print(f"On (insert date here), there were {len(x['league']['games'])} played")
input("Press ENTER key to display game data...")

for game in x["league"]["games"]:
    print("Game stats...")



    hometeamname = requests.get("https://api.sportradar.us/mlb/{access_level}/v7/en/teams/{team_id}/profile.json?api_key={your_api_key}")
    hometeamname = hometeamname.json()
    print(hometeamname)


    print(f"Home team: {game['game']['home_team']}")
    print(f"Away team: {game['game']['away_team']}")
    print()


# this allows a lookup of a team
#https://api.sportradar.us/mlb/{access_level}/{version}/en/teams/{team_id}/profile.{format}?api_key={your_api_key}
