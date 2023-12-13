import re

with open("polski.txt", encoding="UTF-8") as file:
  content = file.read()
  x = re.findall("[a-zA-Z]{6}\w*", content)
  for word in x:
    print(word)