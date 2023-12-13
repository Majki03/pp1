with open("countries.txt") as file:
  counter = 0
  for line in file:
    counter += 1
    print(f"{counter}. {line}", end = "")