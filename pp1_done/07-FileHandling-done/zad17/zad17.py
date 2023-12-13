with open("mbox-short.txt") as file:
  count = 0
  for line in file:
    count += 1
    print(line, end = "")
    if(count == 5):
      input("Press enter to continue...")
      count = 0