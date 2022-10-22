import re

text = input()
# regex = r"\b_([A-Z]|[a-z]|[0-9])+\b"
lst = []
regex = r"\b_([A-Za-z]+|[0-9])+\b"
search_pattern = re.findall(regex, text)

# text -> ['The', '_id', 'and', '_age', 'variables', 'are', 'both', 'integers.']

print(",".join(search_pattern))

