import re

mess = "To be, or not to be, that is the question."
num = re.findall("[a-zA-Z]+", mess)
count = 0

for i in num:
  count += 1
print(count)