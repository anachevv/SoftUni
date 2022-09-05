n_commands = int(input())
reg_numbers = []
for _ in range(n_commands):
    command = input().split(', ')
    direction, reg_number = command
    if direction == 'IN':
        if reg_number not in reg_numbers:
            reg_numbers.append(reg_number)
    elif direction == 'OUT':
        if reg_number in reg_numbers:
            reg_numbers.remove(reg_number)
reg_numbers = set(reg_numbers)
if reg_numbers:
    print("\n".join(reg_numbers))
else:
    print("Parking Lot is Empty")
