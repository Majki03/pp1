class C():
    def __init__(self, coordinates):
        self.coordinates = coordinates
    def m(self, n):
        count = 0
        for x, y in self.coordinates:
            if x > 0 and y > 0:
                count += 1
                if count >= n:
                    return True
        return False

obj = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
print(obj.m(2))
print(obj.m(3))