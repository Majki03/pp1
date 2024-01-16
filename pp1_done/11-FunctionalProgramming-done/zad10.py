distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

def avg_speed(distance, hours, minutes):
    total_time = hours + minutes / 60
    if(total_time == 0):
        return 0
    return distance / total_time

avg = avg_speed(distance, hours, minutes)

print(f"Average speed: {avg:.1f} km/h")