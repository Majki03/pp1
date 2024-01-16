speed_val = [48, 47, 54, 50, 42, 68, 39, 46]

too_high = list(filter(lambda s: s > 50, speed_val))

print(f"Recorded values: {", ".join(map(str, speed_val))}\n"
      f"Speed too high: {", ".join(map(str, too_high))}")