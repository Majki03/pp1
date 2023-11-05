calculate_bmi = lambda weight_kg, height_cm: weight_kg / ((height_cm / 100) ** 2)

peter_weight = 81
peter_height = 182
peter_bmi = calculate_bmi(peter_weight, peter_height)

print(f"Peter's BMI is {peter_bmi:.2f}")