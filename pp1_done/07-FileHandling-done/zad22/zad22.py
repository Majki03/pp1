import random

with open("ran_num.txt", "w") as file:
  for line in range(1, 51):
    file.write(str(random.randint(100, 999))+"\n")