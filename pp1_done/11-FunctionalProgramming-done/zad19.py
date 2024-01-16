grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2, 0]

ex_neg = list(filter(lambda ex: ex > 2.0, grades))

suma = sum(ex_neg)
lenght = len(ex_neg)

print(f"Arthmrtic mean for grades <> 2.0 is {suma / lenght:.2f}")