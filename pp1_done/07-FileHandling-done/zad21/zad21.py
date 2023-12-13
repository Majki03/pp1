with open("num.txt", "w") as file:
  num = 0
  for line in range(1, 51):
    num += 1
    file.write(str(num)+"\n")