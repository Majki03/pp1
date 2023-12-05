tup = (50, 20, 40, 50, 30, 50)
value = 50

count = 0
for i in tup:
    if(i == value):
        count += 1

print("Tuple:", ",".join(map(str, tup)))
print("Value:", value)
print("Number of occurrences:", count)