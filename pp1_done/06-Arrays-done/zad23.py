arr = [-15, 8, -31, 47, -2, 19]

smallest = 0
for i in arr:
    if(i < smallest):
        smallest = i
print(smallest)

biggest = 0
for i in arr:
    if(i > biggest):
        biggest = i
print(biggest)