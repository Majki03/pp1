import matplotlib.pyplot as plt

olympic_medals_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

total_medals = list(map(lambda country: country["gold"] + country["silver"] + country["bronze"], olympic_medals_data))
countries = [country["country"] for country in olympic_medals_data]

plt.figure(figsize=(10, 6))
plt.bar(countries, total_medals, color='blue')
plt.title('Total Number of Medals Won by Each Country')
plt.xlabel('Countries')
plt.ylabel('Total Medals')

plt.show()