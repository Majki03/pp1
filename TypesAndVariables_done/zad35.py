diameter = input("Enter tree diameter: ")

radius = int(diameter) / 2
PI = 3.14

circumference = 2*PI*radius

valid = 157 <= circumference

print("Tree can be cut down:", valid)