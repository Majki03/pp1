numx = input("Enter x: ")
numy = input("Enter y: ")

try:
    x = int(numx)
    y = int(numy)

    if(x > 0 and y > 0):
        print(f"Point P({x}, {y}) is located in the first quadrant of the coordinate system")
    elif(x < 0 and y > 0):
        print(f"Point P({x}, {y}) is located in the second quadrant of the coordinate system")
    elif(x < 0 and y < 0):
        print(f"Point P({x}, {y}) is located in the third quadrant of the coordinate system")
    elif(x > 0 and y < 0):
        print(f"Point P({x}, {y}) is located in the forth quadrant of the coordinate system")
    elif(x == 0 and y < 0 or y > 0):
        print(f"Point P({x}, {y}) is located on the x axis")
    elif(x < 0 or x > 0 and y == 0):
        print(f"Point P({x}, {y}) is located on the y axis")
    elif(x == 0 and y == 0):
        print(f"Point P({x}, {y}) is located in the position (0, 0)")
except:
    print("Invalide value, pleas enter a number")