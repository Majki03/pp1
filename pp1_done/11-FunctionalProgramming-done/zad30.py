bottle_capacity = 500
tolerance = 0.02

filled_bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

def is_incorrectly_filled(capacity, tolerance):
    lower_limit = capacity - capacity * tolerance
    upper_limit = capacity + capacity * tolerance

    def check(filled_volume):
        return not (lower_limit <= filled_volume <= upper_limit)

    return check

check_fill = is_incorrectly_filled(bottle_capacity, tolerance)
incorrectly_filled_bottles = list(filter(check_fill, filled_bottles))

percentage_incorrect = (len(incorrectly_filled_bottles) / len(filled_bottles)) * 100

print(f"Bottle capacity:    {bottle_capacity}ml\n"
      f"Filling tolerance:  {tolerance * 100:.0f}%\n"
      f"Filled bottles:     {",".join(map(str, filled_bottles))}\n"
      f"Incorrectly filled: {percentage_incorrect:.0f}%")