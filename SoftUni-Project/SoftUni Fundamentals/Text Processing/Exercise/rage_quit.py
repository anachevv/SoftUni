text = input()
substring = ""
new_text = ""

for element in range(len(text)):
    number = ''
    if not text[element].isdigit():
        substring += text[element]
    if text[element].isdigit():
        while element < len(text) and text[element].isdigit():
            number += text[element]
            element += 1
        number = int(number)
        new_text += substring.upper() * number
        substring = ""
        continue
print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)
