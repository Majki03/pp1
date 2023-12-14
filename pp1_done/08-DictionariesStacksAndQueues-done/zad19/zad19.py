import json

with open("students.json", "r") as file:
  load = json.load(file)

limited = [{
  "first_name":student["name"],
  "last_name":student["surname"],
  "student_id":student["student ID"]
  } for student in load]

with open("limited.json", "w") as copy:
  json.dump(limited, copy, indent = 2)