import json

with open("dwsample3-json.json") as file:
  data = json.load(file)
  
for key, value in data.items():
  print(f"{key}: {value}")