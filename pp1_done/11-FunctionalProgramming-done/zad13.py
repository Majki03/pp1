def check_fill(capacity):
    if capacity == 500:
        tolerance = 0.02
    elif capacity == 1000:
        tolerance = 0.03
    elif capacity == 1500:
        tolerance = 0.05
    else:
        raise ValueError("Unsupported capacity")

    def check(amount):
        lower_limit = capacity - capacity * tolerance
        upper_limit = capacity + capacity * tolerance
        return lower_limit <= amount <= upper_limit

    return check

check_500ml = check_fill(500)
check_1000ml = check_fill(1000)
check_1500ml = check_fill(1500)

print(f"507: {check_500ml(507)}\n"
      f"489: {check_500ml(489)}\n"
      f"984: {check_1000ml(984)}\n"
      f"1032: {check_1000ml(1032)}\n"
      f"1578: {check_1500ml(1578)}\n"
      f"1430: {check_1500ml(1430)}")