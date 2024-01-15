class Phone():
    def __init__(self, brand, year, like):
        self.brand = brand
        self.year = year
        self.like = like
        self.open = False
    def on(self):
        self.open = True
    def off(self):
        self.open = False

my_phone = Phone("Samsung", 2023, "Yes")

print(f"My phone is {my_phone.brand}. It came out in year {my_phone.year}. Do I like it? {my_phone.like}!")

my_phone.on()

if(my_phone.on):
    print("I'am actually looking at my phone.")
else:
    print("I don't have time now to look at my phone.")