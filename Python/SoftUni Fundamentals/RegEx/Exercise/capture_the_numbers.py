import re

lst = []

while True:
    text = input()
    if text == "":
         break
    regex = r"\d+"
    search_pattern = re.findall(regex, text)
    for match in search_pattern:
        lst.append(match)

print(" ".join(lst))

