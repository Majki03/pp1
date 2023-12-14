student = {
  "name":"Michal",
  "surname":"Cudzich",
  "age":20,
  "university":"Krakow University of Economics",
  "subject":"Applied Informatics",
  "years":{"year":1, "term":1},
  "acctive":True
}

import json

with open("student.json", "w") as file:
  json.dump(student, file, indent=2)