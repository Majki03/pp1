height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

height_m = height / 100

BMI = weight / height_m**2

range = 25 <= BMI <= 29

print("Your BMI index:", BMI)
print("Correct weight:", range)