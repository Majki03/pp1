car_speed = input("Enter car speed: ")

speed_limit_min = 40
speed_limit_max = 140

try:
    if(int(car_speed) < speed_limit_min or int(car_speed) > speed_limit_max):
        print("Warning: invalid car speed!")
except:
    print("Invalid value, please enter number")