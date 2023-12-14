import json

movie = {
  "title":"The Wolf of Wall Street",
  "year":2013,
  "actor":{"leading":"Leonardo DiCaprio", "supporting":"Margot Robbie"},
  "oscar":False,
  "genre":"Criminal/Comedy",
}

with open("favourite.json", "w") as file:
  json.dump(movie, file, indent=2)