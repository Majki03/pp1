eur = [15.90, 38.47, 4.07, 132.70, 9.15]
pln = list(map(lambda x:x*4.5, eur))

pln_values = '\n'.join(f"{value:.2f}" for value in pln)

print(pln_values)