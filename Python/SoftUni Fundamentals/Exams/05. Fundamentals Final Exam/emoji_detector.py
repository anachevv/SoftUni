import re

text = input()
numbers = [int(element) for element in text if element.isdigit()]
cool_threshold = 1
for number in numbers:
    cool_threshold *= number

regex = r"(?P<Separator>::|\*\*)(?P<Name>[A-Z]{1}[a-z]{2,})(?P=Separator)"
emojis = [data.groupdict() for data in re.finditer(regex, text)]
all_emojis = len(emojis)

print(f"Cool threshold: {cool_threshold}\n{all_emojis} emojis found in the text. The cool ones are:")

for element in emojis:
    threshold_sum = sum([ord(letter) for letter in element["Name"]])
    if threshold_sum > cool_threshold:
        print(f'{element["Separator"]}{element["Name"]}{element["Separator"]}')
