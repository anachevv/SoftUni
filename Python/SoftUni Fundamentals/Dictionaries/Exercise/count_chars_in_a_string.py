string = input()
dct = {char: string.count(char) for char in string if char != ' '}

for key, value in dct.items():
    print(f"{key} -> {value}")
