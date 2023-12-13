first = "How to train your dragon"
second = "Mission Impossible"
third = "Spider-Man"
forth = "Inception"
fifth = "Barbie"

with open("movies.txt", "w") as file:
  file.write(first+"\n")
  file.write(second+"\n")
  file.write(third+"\n")
  file.write(forth+"\n")
  file.write(fifth+"\n")