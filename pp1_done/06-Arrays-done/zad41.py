def is_sub(array1, array2):
    return all(i in array2 for i in array1)

arr1 = [1, 3, 6, 8, 13, 4, 9]
arr2 = [3, 5, 8, 1, 9, 0, 13, 6, 4]

result = is_sub(arr1, arr2)

if(result):
    print("Array1 is a subset od Array2")
else:
    print("Array1 is not a subset of Array2")