time_24 = input("Enter time (24-hour format): ")

if(float(time_24) < 13 and float(time_24) >= 0):
    print(f"Time in 12-hour format: {time_24[:1]}:{time_24[2:]}am")
elif(float(time_24) >= 13 and float(time_24) <= 24):
    time_12 = int(time_24[:2]) - 12
    print(f"Time in 12-hour format: {time_12}:{time_24[3:]}pm")