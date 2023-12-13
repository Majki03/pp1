import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)

for temp in range(1):
  print(" ".join(map(str, temperatures)))