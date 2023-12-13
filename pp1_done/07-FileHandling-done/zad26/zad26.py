import re

mess = "To be, or not to be, that is the question"
vowels = re.findall("[aeiou]", mess)
count = 0

for i in vowels:
  count += 1
print(count)