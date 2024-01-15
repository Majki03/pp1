class TV():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.is_on = False
        self.show_status = "TV is off"
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
        self.show_status = print(f"TV is on, channel {self.channel_no}")
    def turn_off(self):
        self.is_on = False
        self.show_status = "TV is off"
    def change_channel(self, channel):
        self.channel_no = channel

tv = TV("Samsung", "Black")

print(tv.show_status)

tv.turn_on()

tv.change_channel(5)
tv.turn_on()

tv.turn_off()
print(tv.show_status)