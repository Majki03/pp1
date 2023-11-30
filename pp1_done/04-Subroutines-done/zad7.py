def f():
  height = cm / 100
  BMI = weight / height**2
  return BMI
  
name = input("Enter name: ")
weight = int(input("Enter weight (kg): "))
cm = int(input("Enter height (cm): "))

print(f"{name}'s BMI is", f())