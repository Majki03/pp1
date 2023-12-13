name = "Michal Cudzich"
university = "Krakow Univesity of Economics"
field = "Applied Informatics"

with open("student.txt", "w") as file:
  file.write(name+"\n")
  file.write(university+"\n")
  file.write(field+"\n")