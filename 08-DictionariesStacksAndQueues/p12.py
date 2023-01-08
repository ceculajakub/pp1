import json

film = {
    "genre":"drama",
    "cast": 12,
    "length":120,
    "rating": 7.2,
    "title":"USA"
}
file = open("favourite.json", "a")
json.dump(film, file, indent=2)
