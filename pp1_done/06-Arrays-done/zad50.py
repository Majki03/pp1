arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest = 0
location = None

for i in range(len(arr)):
    for j in range(len(arr[i])):
        current = arr[i][j]
        if(current < smallest):
            smallest = current
            location = (i, j)

print(smallest)
print(location)