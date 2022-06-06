string_with_information = input().split('#')    # First example: ['High = 89', 'Low = 28', 'Medium = 77', 'Low = 23']
water_available = int(input())

total_fire = 0
effort = 0

list_with_valid_cells = []

for cell in range(len(string_with_information)):

    if water_available <= 0:
        break

    level, fire = string_with_information[cell].split(' = ')
    fire = int(fire)

    if fire > water_available:
        continue

    if level == 'High':
        if 81 <= fire <= 125:
            water_available -= fire
            total_fire += fire
            effort += 0.25 * fire

            list_with_valid_cells.append(fire)
    elif level == 'Medium':
        if 51 <= fire <= 80:
            water_available -= fire
            total_fire += fire
            effort += 0.25 * fire

            list_with_valid_cells.append(fire)
    elif level == 'Low':
        if 1 <= fire <= 50:
            water_available -= fire
            total_fire += fire
            effort += 0.25 * fire

            list_with_valid_cells.append(fire)

print('Cells:')

for index in list_with_valid_cells:
    print(f' - {index}')


print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
