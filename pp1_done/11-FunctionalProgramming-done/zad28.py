medals = [{"country":"Denmark", "gold":2, "silver":4, "bronze":6},
          {"country":"Finland", "gold":5, "silver":0, "bronze":4},
          {"country":"USA", "gold":12, "silver":5, "bronze":11},
          {"country":"Peru", "gold":0, "silver":1, "bronze":7}]

won = filter(lambda country: country["gold"] + country["silver"] + country["bronze"] >= 10, medals)

with_10 = [f"{country["country"]}: {country["gold"]},{country["silver"]},{country["bronze"]}" for country in won]

print("COUNTRIES WITH AT LEAST 10 MEDALS")
print("\n".join(with_10))