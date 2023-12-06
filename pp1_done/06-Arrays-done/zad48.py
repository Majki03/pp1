def create_2d_arr(x, y):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def display_2d_arr(arr):
    for row in arr:
        print(row)

rows, cols = 3, 5

arr_2d = create_2d_arr(rows, cols)

print(display_2d_arr(arr_2d))