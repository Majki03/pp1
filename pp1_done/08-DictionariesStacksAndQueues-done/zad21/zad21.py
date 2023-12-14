import csv
import json

products_data = []

with open("products.csv") as file:
  read = csv.DictReader(file)
  for row in read:
    products_data.append(row)
    
with open("products.json", "w") as copy:
  json.dump(products_data, copy, indent = 2)