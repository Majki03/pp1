def transpose_matrix(m):
    transposed_matrix = list(map(list, zip(*m)))
    return transposed_matrix

def display(array):
    for row in array:
        print(" ".join(map(str, row)))