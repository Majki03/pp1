total = int(input("Enter the total number of test tasks: "))
completed = int(input("Enter the number of correctly completed tasks: "))

pass_p = (completed / total) * 100

if pass_p >= 50:
    print(f"The test is passed with a pass percentage of {pass_p:.2f}%.")
else:
    print(f"The test is not passed with a pass percentage of {pass_p:.2f}%.")