employees = [("Smith", "Lucy"),  ("Jones", "Janet"), ("Lee", "Jerry"), ("Jackson", "Peter"), ("Johnson", "Rick"), ("Lewis", "Terry"), ("Clarke", "Robin")]

name = list(map(lambda nm: f"{nm[0].upper()}, {nm[1]}", employees))

print("\n".join(name))