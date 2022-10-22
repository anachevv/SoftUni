def squeeze(text):
    for char in text:
        while char * 2 in text:
            text = text.replace(char * 2, char)

    return text


text = input()

print(squeeze(text))
