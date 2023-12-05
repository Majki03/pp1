arr = [12, 6, 4, 9, 10]

def star(n):
    for i in arr:
        if(i == n):
            return "*" * i

result1 = star(arr[0])
result2 = star(arr[1])
result3 = star(arr[2])
result4 = star(arr[3])
result5 = star(arr[4])

print("12:", result1)
print("6:", result2)
print("4:", result3)
print("9:", result4)
print("10:", result5)