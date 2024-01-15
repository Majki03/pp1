class Cellphone():
    def __init__(self, brand, color, year, wallpaper):
        self.brand = brand
        self.color = color
        self.year = year
        self.is_on = False
        self.wallpaper = wallpaper
    def status_on(self):
        self.is_on = True
        self.status = "On"
    def status_off(self):
        self.is_on = False
        self.status = "Off"
    def change_wallpaper(self, change):
        self.wallpaper = change
    
phone1 = Cellphone("Samsung", "Black", 2023, "Black")
phone2 = Cellphone("iPhone", "White", 2020, "White")

phone1.status_on()
print(phone1.status)

print(phone1.wallpaper)

phone1.change_wallpaper("Green")
print(phone1.wallpaper)