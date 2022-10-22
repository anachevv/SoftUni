import re

text = input()
regex = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"

search_pattern = re.findall(regex, text)

print(' '.join(search_pattern))
