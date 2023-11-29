name = input("Enter name: ")
l_name = name.lower()

if(l_name.endswith("a")):
    print(f"{name} - Polish female name")
else:
    print("Not a polish female name")