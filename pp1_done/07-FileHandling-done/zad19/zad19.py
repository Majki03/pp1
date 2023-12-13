with open("copylines.txt", "w") as copy:
  with open("polski.txt") as file:
    for line in file:
      line = file.read()
      copy.write(line)