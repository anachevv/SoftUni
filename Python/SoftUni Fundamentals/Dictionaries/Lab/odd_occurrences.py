sequence_of_words = [word.lower() for word in input().split()]
dct = {word: sequence_of_words.count(word) for word in sequence_of_words}

for key, value in dct.items():
    if value % 2 != 0:
        print(key, end=" ")
