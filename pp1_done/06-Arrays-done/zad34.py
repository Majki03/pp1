tup = (10, 20, 30, 40, 50)
print("Tuple:", ",".join(map(str, tup)))

reverse = tuple(reversed(tup))
print("Reverse order:", ",".join(map(str, reverse)))