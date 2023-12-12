import re

regu = input("Podaj wyrażenie regularne: ")

try:
    with open("mbox.txt") as file:
        count = 0
        for line in file:
            x = re.findall(regu, line)
            if(not x):
                continue
            else:
                count += 1
        print(f"mbox.txt ma {count} linii, które pasują do {regu}")
except:
    print("Podaj wyrażenie regularne")