import re

with open("grades.txt", "r") as file:
  content = file.read()

  grades_match = re.search(r'Grades: (.+)', content)
        
  if grades_match:
    grades_line = grades_match.group(1)
    grades = [float(grade) for grade in re.findall(r'\d+\.\d+', grades_line)]

    mean_grade = sum(grades) / len(grades)

    print(f"The arithmetic mean of {re.search(r'Name: (.+)', content).group(1)}'s grades is: {mean_grade:.2f}")