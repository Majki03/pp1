def chop():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = l1.remove(1)
    l2 = l1.remove(6)
    return l2

def middle():
    l3 = [1, 2, 3, 4, 5, 6]
    l4 = l3.pop(0)
    l4 = l3.pop(4)
    return l3

resul1 = chop()
resul2 = middle()

print(resul1)
print(resul2)