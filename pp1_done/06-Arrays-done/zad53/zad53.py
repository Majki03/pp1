import matrix

arr_3 = matrix.identity_matrix(3)
arr_5 = matrix.identity_matrix(5)
arr_8 = matrix.identity_matrix(8)

result_3 = matrix.display_matrix(arr_3)
result_5 = matrix.display_matrix(arr_5)
result_8 = matrix.display_matrix(arr_8)

if(__name__ == "__main__"):
    print(result_3)
    print(result_5)
    print(result_8)