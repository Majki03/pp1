def bubblesort(array):
    n = len(array)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return
        
arr1 = [12, 312, 34, 1, 3, 5, 6, 30, 634]
arr2 = [1, 4, 1234, 41, 24, 11, 23, 7]
arr3 = [123, 7, 12, 2, 2314, 9, 56]

bubblesort(arr1)
bubblesort(arr2)
bubblesort(arr3)

for i in range(len(arr1)):
    print(arr1[i], end=" ")
print("")

for i in range(len(arr2)):
    print(arr2[i], end=" ")
print("")

for i in range(len(arr3)):
    print(arr3[i], end=" ")