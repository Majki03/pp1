import math

circumference = float(input("Enter tree circumference: "))
Pi = math.pi

diameter = circumference / Pi

if(diameter >= 50):
    print("Tree can be cut down: True")
else:
    print("Tree can be cut down: False")