with open("copy.txt", "w") as copy:
  f = open("polski.txt")
  read = f.read()
  copy.write(read)
  f.close()