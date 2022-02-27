import json

filename = 'chapter_10/usernames.json'

with open(filename) as f_object:
    username = json.load(f_object)
    print(f"Welcome back {username}!")