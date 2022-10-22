import re


def count(words, text):
    dct = {}
    words_file = open(words, 'r')
    regex = r'[a-zA-z\']+'

    for line in words_file:
        for word in line.split():
            dct[word.lower()] = 0

    text_file = open(text, 'r')
    file_content = ""

    for line in text_file:
        for word in line.split():
            file_content += word + ' '

    file_content = file_content.lower().strip()
    pattern = re.findall(regex, file_content)

    for word in pattern:
        if word in dct:
            dct[word] += 1

    dct = sorted(dct.items(), key=lambda x: (-x[1]))
    result = ""

    for info in dct:
        word, value = info[0], info[1]
        result += f"{word} - {value}" + '\n'

    return result


words_to_find = "./words.txt"
text = "./text.txt"

print(count(words_to_find, text))