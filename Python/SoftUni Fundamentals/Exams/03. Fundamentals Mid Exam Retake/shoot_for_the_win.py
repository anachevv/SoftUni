sequence_of_numbers = [int(x) for x in input().split()]
command = input()

total_targets = []
count = -1
while command != 'End':
    if command == 'End':
        break

    command = int(command)

    if 0 <= command < len(sequence_of_numbers):
        target = sequence_of_numbers[command]
        temporary = target
        value = sequence_of_numbers[command]
        if value not in total_targets:
            value = -1
            total_targets.append(value)
            for current_target in sequence_of_numbers:
                if current_target > value:
                    current_target -= value
                else:
                    current_target += value
    else:
        count += 1
        target = sequence_of_numbers[count]
        temporary = target
        value = sequence_of_numbers[count]
        if value not in total_targets:
            value = -1
            total_targets.append(value)
            for current_target in sequence_of_numbers:
                if current_target > value:
                    current_target -= value
                    total_targets.append(current_target)
                else:
                    total_targets.append(current_target)

    command = input()

print(f"Shot targets: {len(sequence_of_numbers)} -> " + " ".join(str(x) for x in sequence_of_numbers))
