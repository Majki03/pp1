with open("studentslist.txt") as file:
  for line in file:
    line = line.rstrip()
    line_list = line.split(",")
    if(not int(line_list[2]) < 30):
      continue
    else:
      print(f"{line_list[0]}  {line_list[1]}  {line_list[4]}")