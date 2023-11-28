height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

height_m = height / 100
bmi = weight / height_m**2

if(bmi >= 18.5 and bmi <= 24.99):
    print(f"Your BMI index: {bmi:.2f}")
    print("Correct weight: True")
else:
    print(f"Your BMI index: {bmi:.2f}")
    print("Correct weight: False")