from fileinput import filename
import json

filename = 'chapter_10/numbers.json'

with open(filename) as f_object:
    numbers = json.load(f_object)

print(numbers)