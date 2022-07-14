def emoticon_finder(text):
    string_of_emoticons = ""

    for char in text:
        if char == ':':
            colon_index = [index for (index, n) in enumerate(text) if n == ':']
            string_of_emoticons = [text[symbol] + text[symbol + 1] for symbol in colon_index]

    return "\n".join(string_of_emoticons)


text = input()

print(emoticon_finder(text))
