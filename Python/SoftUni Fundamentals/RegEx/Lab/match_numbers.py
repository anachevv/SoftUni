import re

text = input()

regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

search_pattern = re.finditer(regex, text)

for match in search_pattern:
    print(match.group(), end=" ")

