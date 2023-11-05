registration = input("Enter vehicle registration number: ")

is_from_krakow = registration.startswith("KR") or registration.startswith("KK")

print("Is the registration from Krakow?", is_from_krakow)