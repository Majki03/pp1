def compare(array1, array2):
    if(array1 == array2):
        return True
    else:
        return False
    
arr1 = ["water", "book", "sky"]
arr2 = ["water", "book", "sky"]
arr3 = ["True", "False"]
arr4 = ["True", "False", "True"]
arr5 = [5, 3, 1]
arr6 = [5, 3, 1]
arr7 = [3, 2, 1]
arr8 = [3, 2]

result1 = compare(arr1, arr2)
result2 = compare(arr3, arr4)
result3 = compare(arr5, arr6)
result4 = compare(arr7, arr8)

print("Array1:", " ".join(map(str, arr1)))
print("Array2:", " ".join(map(str, arr2)))
print("Comparison:", result1)
print("Array1:", " ".join(map(str, arr3)))
print("Array2:", " ".join(map(str, arr4)))
print("Comparison:", result2)
print("Array1:", " ".join(map(str, arr5)))
print("Array2:", " ".join(map(str, arr6)))
print("Comparison:", result3)
print("Array1:", " ".join(map(str, arr7)))
print("Array2:", " ".join(map(str, arr8)))
print("Comparison:", result4)