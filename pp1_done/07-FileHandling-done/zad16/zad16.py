name = input("Enter file name: ")

try:
  with open(name) as file:
    count = 0
    for line in file:
      count += 1
    print("Number of lines:", count)
except:
  print("Wrong file name")