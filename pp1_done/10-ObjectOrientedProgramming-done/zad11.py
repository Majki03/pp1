class TV():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.is_on = False
        self.show_status = "TV is off"
    def turn_on(self):
        self.is_on = True
        self.show_status = "TV is on"
    def turn_off(self):
        self.is_on = False
        self.show_status = "TV is off"

tv = TV("Samsung", "Black")

print(tv.show_status)

tv.turn_on()
print(tv.show_status)

tv.turn_off()
print(tv.show_status)