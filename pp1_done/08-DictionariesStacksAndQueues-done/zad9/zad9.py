countries = [
  {"name":"Poland", "population":38000000},
  {"name":"Germany", "population":83000000},
  {"name":"Canada", "population":38000000},
  {"name":"USA", "population":332000000},
  {"name":"Japan", "population":126000000}
  ]
  
print("COUNTRY  POPULATION")

i = 0
while i < len(countries):
  country = countries[i]["name"]
  population = countries[i]["population"]
  print(f"{country:<9}{population}")
  i += 1