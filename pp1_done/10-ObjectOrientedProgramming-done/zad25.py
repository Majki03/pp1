class C():
    def __init__(self, sectors):
        self.sectors = sectors
    def m1(self, s, n):
        self.sectors[s] = n
    def m2(self, s):
        return sum(self.sectors[sector] for sector in s if sector in self.sectors)

stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
stadium.m1("G", 130)
result_gd = stadium.m2("GD")
result_kej = stadium.m2("KEJ")

print("Sum of fans in sectors GD:", result_gd)
print("Sum of fans in sectors KEJ:", result_kej)