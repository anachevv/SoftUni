import re

text = input()
regex = r"(?<=\s)(([a-z0-9]+[\-\._a-z0-9]*)@[a-z\-]+(\.[a-z\-]+)+)\b"
search_pattern = re.findall(regex, text)

for match in search_pattern:
    print(match[0])
