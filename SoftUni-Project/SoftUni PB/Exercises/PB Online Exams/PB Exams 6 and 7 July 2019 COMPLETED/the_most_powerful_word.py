import math

word = input()
vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
points = 0
total_points = 0
string_word = ""

while word != "End of words":

    for letter in word:
        points += ord(letter)

    if word[0] in vowels:
        points *= len(word)
    else:
        points /= math.floor(len(word))

    if total_points < points:
        total_points = points
        string_word = word

    points = 0
    word = input()

print(f"The most powerful word is {string_word} - {total_points}")
