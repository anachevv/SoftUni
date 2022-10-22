text = input()
chars = sorted(set(char for char in text))
for char in chars:
    print(f"{char}: {text.count(char)} time/s")
