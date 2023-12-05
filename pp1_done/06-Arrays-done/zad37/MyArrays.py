def s_large(array):
    s_largest = 0
    for i in array:
        if(i > s_largest and i < max(array)):
            s_largest = i
    return s_largest

def diff(array):
    maxi = max(array)
    mini = min(array)
    return maxi - mini

def med(array):
    if(len(array) % 2 != 0):
        mid = len(array) // 2
        medi = array[mid]
        return medi
    else:
        mid = len(array) // 2
        mid_1 = (len(array) // 2) - array[mid + 2]
        medi = (array[mid] + array[mid_1]) / 2
        return medi

def s_a_l(array):
    maxi = max(array)
    mini = min(array)
    return mini, maxi

def string(array):
    return "-".join(map(str, array))

arr = [7, 3, 8, 5, 2]

result = s_large(arr)
result1 = diff(arr)
result2 = med(arr)
result3 = s_a_l(arr)
result4 = string(arr)

if __name__ == "__main__":
    print("Numbers:", ",".join(map(str, arr)))
    print("Second largest number:", result)
    print("Diffrence between the largest and smallest value:", result1)
    print("Median:", result2)
    print("Smallest and largest number:", result3)
    print("Numbers as a string:", result4)