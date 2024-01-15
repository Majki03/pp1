class TV():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.channels = list("")
        self.is_on = False
        self.show_status = "TV is off"
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
        if self.is_on:
            channel_name = self.channels[self.channel_no - 1] if self.channel_no <= len(self.channels) else "Unknown"
            print(f"TV is on, channel {self.channel_no} ({channel_name})")
    def turn_off(self):
        self.is_on = False
        self.show_status = "TV is off"
    def change_channel(self, channel):
        self.channel_no = channel
    def set_channels(self, channels_list):
        self.channels = channels_list
        self.show_channels = print(f"Channel list:\n"
                                   f"1. {self.channels[0]}\n"
                                   f"2. {self.channels[1]}\n"
                                   f"3. {self.channels[2]}\n"
                                   f"4. {self.channels[3]}\n"
                                   f"5. {self.channels[4]}\n"
                                   f"6. {self.channels[5]}")

tv = TV("Samsung", "Black")

tv.turn_on()

tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])

tv.change_channel(4)

tv.turn_on()