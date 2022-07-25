import re

text = input().lower()
special_word = input().lower()
regex = rf"\b{special_word}\b"
search_pattern = re.findall(regex, text)

print(len(search_pattern))
