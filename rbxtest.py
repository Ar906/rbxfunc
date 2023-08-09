
import requests

place_id = 369764591  # User ID
user_req = requests.get(f"https://apis.roblox.com/universes/v1/places/{place_id}/universe")
user_data = user_req.json()

uni_id = user_data["universeId"]
game_check = requests.get(f"https://games.roblox.com/v1/games?universeIds={uni_id}")
game_data = game_check.json()
stats = game_data["data"]

print(game_data["data"][0]["visits"])