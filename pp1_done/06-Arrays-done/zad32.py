def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
arr = [15, 38, 7, 23, 14]

num = int(input("Enter number: "))

result = occurs(num, arr)

print("Number:", num)
print("Array:", " ".join(map(str, arr)))
if(result == True):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} do not appears in the array")