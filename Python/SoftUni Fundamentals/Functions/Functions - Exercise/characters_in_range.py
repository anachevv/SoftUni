def characters_in_range(first, second):

    lst = []

    for current_character in range(ord(first_character) + 1, ord(second_character)):
        lst.append(chr(current_character))

    return ' '.join(character for character in lst)


first_character = input()
second_character = input()

print(characters_in_range(first_character, second_character))
