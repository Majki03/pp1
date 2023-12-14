import json

with open("euro.json") as file:
  load = json.load(file)
  
print("Date      Buying Rate     Selling Rate")
print("=" * 40)

for rate in ["rates"]:
  date = rate["effectiveDate"]
  buying_rate = rate["bid"]
  selling_rate = rate["ask"]
  print(f"{date}{buying_rate:<10}{selling_rate}")