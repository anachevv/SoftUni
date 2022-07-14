def replace_chars(text):
    import re

    for char in text:
        text = re.sub(fr"\\{char}+", f"{char}", text)

    return text


string = input()

print(replace_chars(string))
