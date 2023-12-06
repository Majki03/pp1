def identity_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def display_matrix(array):
    for i in range(len(array)):
        array[i][i] = 1
    for row in array:
        print(" ".join(map(str, row)))