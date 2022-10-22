import re

participants = input().split(', ')
text = input()
regex = r"\w+"
info = {}
while text != 'end of race':
    search_pattern = re.findall(regex, text)
    name = ""
    distance = 0
    for match in search_pattern:
        for char in match:
            if char.isalpha():
                name += char
            else:
                distance += int(char)
    if name in participants:
        if name not in info:
            info[name] = 0
        info[name] += distance
    text = input()

info = {name: distance for (name, distance) in sorted(info.items(), key=lambda item: item[1], reverse=True)}
count = 0
for name, distance in info.items():
    count += 1
    if count > 3:
        break
    elif count == 1:
        print(f"{count}st place: {name}")
    elif count == 2:
        print(f"{count}nd place: {name}")
    elif count == 3:
        print(f"{count}rd place: {name}")
