movie = {
  "title":"The Wolf of Wall Street",
  "year":2013,
  "actor":{"leading":"Leonardo DiCaprio", "supporting":"Margot Robbie"},
  "oscar":False,
  "genre":"Criminal/Comedy",
}

count = 0
for key, value in movie.items():
  if(key):
    count += 1
print(count)