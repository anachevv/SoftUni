n_number = int(input())
dct = {}

for _ in range(n_number):
    word = input()
    synonym = input()
    if word not in dct:
        dct[word] = []
    dct[word].append(synonym)

for word in dct:
    print(f"{word} - {', '.join(dct[word])}")
