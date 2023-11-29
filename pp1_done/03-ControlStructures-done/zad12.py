f_name = input("Enter first person name: ")
f_age = int(input("Enter first person age: "))
s_name = input("Enter second person name: ")
s_age = int(input("Enter second person age: "))

if(f_age >= 18 and s_age >= 18):
    print(f"Both {f_name} and {s_name} are adults.")
else:
    print("Only one of them or none are adults")