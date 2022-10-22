import re

text = input()
regex = r"([\@\#]+([a-z]{3,})[\@\#]+[^A-Za-z0-9]*[/]+(\d+)[/]+)"
search_pattern = re.findall(regex, text)

for match_tuple in search_pattern:
    amount = match_tuple[-1]
    color = match_tuple[1]
    print(f"You found {amount} {color} eggs!")
