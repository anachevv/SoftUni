string = input()
digits = ""
letters = ""
other = ""

for char in string:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        other += char

print(digits)
print(letters)
print(other)
