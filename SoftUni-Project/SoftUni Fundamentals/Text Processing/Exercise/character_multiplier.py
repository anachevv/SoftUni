def sum_func(first_word, second_word):
    total_sum = 0
    for i in range(len(first_word)):
        if i < len(second_word):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        else:
            total_sum += ord(first_word[i])

    return total_sum


def multiplication(first_word, second_word):
    if len(first_word) > len(second_word):
        result = sum_func(first_word, second_word)
    else:
        result = sum_func(second_word, first_word)

    return result


first_word, second_word = input().split()

print(multiplication(first_word, second_word))
