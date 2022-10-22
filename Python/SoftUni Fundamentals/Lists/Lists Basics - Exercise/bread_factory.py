energy = 100
coins = 100

working_day_events = input().split('|')
all_events_are_handled = True

for current_event in range(len(working_day_events)):

    event, number = working_day_events[current_event].split('-')
    number = int(number)
    if event == 'rest':
        temp = energy
        energy += number

        if energy > 100:
            energy = 100
        gained_energy = energy - temp
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print(f'You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            all_events_are_handled = False
            break

if all_events_are_handled:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
