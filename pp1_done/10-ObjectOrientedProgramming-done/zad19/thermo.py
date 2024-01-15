import random

class Thermometer():
    def __init__(self):
        self.temp = 0
    
    def fever(self):
        self.temp = random.uniform(34, 42)
        if(self.temp > 37 and self.temp < 41):
            print(f"Temperature: {self.temp:.1f} (fever)")
        elif(self.temp > 41):
            print("CRITICAL TEMPERATURE!!!")
        else:
            print(f"Temperature: {self.temp:.1f}")