class Statistics():
    def __init__(self):
        self.numbers = []
    def add_number(self, number):
        self.numbers.append(number)
    def display_numbers(self):
        return " ".join(str(num) for num in self.numbers)
    def max_number(self):
        return max(self.numbers) if self.numbers else None
    def min_number(self):
        return min(self.numbers) if self.numbers else None
    def mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else None
    def median(self):
        sorted_nums = sorted(self.numbers)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    def display_stats(self):
        return (f"Min: {self.min_number()}, Max: {self.max_number()}, "
                f"Mean: {self.mean()}, Median: {self.median()}")

stats = Statistics()

numbers = [12, 37, 6, 9, 17]
for num in numbers:
    stats.add_number(num)

print("Numbers:", stats.display_numbers())
print("Statistics:", stats.display_stats())
