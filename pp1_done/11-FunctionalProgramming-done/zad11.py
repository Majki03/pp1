distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

total_time = hours + minutes / 60

avg = lambda distance, total_time: distance / total_time

result = avg(distance, total_time)

print(f"Average speed: {result:.1f} km/h")