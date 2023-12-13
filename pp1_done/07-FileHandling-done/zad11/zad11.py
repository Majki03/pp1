with open("numbers.txt") as file:
  suma = 0
  for line in file:
    suma += int(line)
    print("Numbers:", file.read())
  print("Sum:", suma)