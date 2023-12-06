import transposed

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
c = [[5, 6, 7, 8]]

tran_a = transposed.transpose_matrix(a)
tran_b = transposed.transpose_matrix(b)
tran_c = transposed.transpose_matrix(c)

dis_a = transposed.display(tran_a)
dis_b = transposed.display(tran_b)
dis_c = transposed.display(tran_c)

print(dis_a)
print(dis_b)
print(dis_c)