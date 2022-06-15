sequence_of_numbers = input().split(' ')
k_number = int(input())

len_of_sequence_of_numbers = len(sequence_of_numbers)
result = []

index = 0
count = 1

while sequence_of_numbers:
    new_list = []

    for i, char in enumerate(sequence_of_numbers):
        person = sequence_of_numbers[i]

        if count % k_number == 0:
            result.append(int(person))
        else:
            new_list.append(person)

        count += 1

    sequence_of_numbers = new_list

    index = (index + 1) % len_of_sequence_of_numbers

print(str(result).replace(' ', ''))
