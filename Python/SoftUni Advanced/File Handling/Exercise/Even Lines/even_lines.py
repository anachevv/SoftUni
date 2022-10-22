def even(file):
    result = ""
    symbols = ["-", ",", ".", "!", "?"]

    with open(file, 'r') as f:
        text = f.readlines()

    for row in range(0, len(text), 2):
        for symbol in symbols:
            text[row] = text[row].replace(symbol, '@')

        result += " ".join(text[row].split()[::-1]) + '\n'

    f.close()

    return result


path = "even-lines.txt"

print(even(path))
