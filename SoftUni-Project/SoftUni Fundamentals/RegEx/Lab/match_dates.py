import re

text = input()

regex = r"\b(?P<day>\d{2}([/.-])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4}))\b"
search_pattern = re.findall(regex, text)

for match in search_pattern:
    day = match[0][0:2]
    month = match[0][3:6]
    year = match[0][7:11]

    print(f"Day: {day}, Month: {month}, Year: {year}")

