import re

text = input()
regex = r"\b((www\.)([A-Za-z0-9\-]+)(\.[a-z]+)+)\b"

links = []
while text != '':
    search_pattern = re.search(regex, text)
    if search_pattern:
        link = search_pattern.group(0)
        links.append(link)
    text = input()

for link in links:
    print(link)
