first_sequence = set([int(num) for num in input().split()])
second_sequence = set([int(num) for num in input().split()])
n_lines = int(input())
for _ in range(n_lines):
    command = input().split()
    if 'Add' in command:
        numbers_to_add = [int(x) for x in command[2::]]
        if 'First' in command:
            for number in numbers_to_add:
                first_sequence.add(number)
        elif 'Second' in command:
            for number in numbers_to_add:
                second_sequence.add(number)
    elif 'Remove' in command:
        numbers_to_remove = [int(x) for x in command[2::]]
        if 'First' in command:
            for number in numbers_to_remove:
                if number in first_sequence:
                    first_sequence.remove(number)
        elif 'Second' in command:
            for number in numbers_to_remove:
                if number in second_sequence:
                    second_sequence.remove(number)
    elif 'Check' in command:
        first_is_subset = first_sequence.issubset(second_sequence)
        second_is_subset = second_sequence.issubset(first_sequence)
        if any([first_is_subset, second_is_subset]):
            print('True')
        else:
            print('False')
first_sequence = sorted(first_sequence)
second_sequence = sorted(second_sequence)

print(', '.join(str(num) for num in first_sequence))
print(', '.join(str(num) for num in second_sequence))
