arr = [15, 8, 31, 47, 2, 19]

suma = 0
index = 0
while index < len(arr):
    suma += arr[index]
    index += 1

art_mean = suma / len(arr)

print(art_mean)