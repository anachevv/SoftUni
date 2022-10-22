n_heroes = int(input())
information = {}
for hero in range(n_heroes):
    text = input().split()
    name, health, mana = text[0], int(text[1]), int(text[2])
    if name not in information:
        information[name] = [health, mana]
        if information[name][0] > 100:
            information[name][0] = 100
        if information[name][1] > 200:
            information[name][1] = 200

command = input()
while command != 'End':
    if 'CastSpell' in command:
        command = command.split(' - ')
        name, mana_needed, spell = command[1], int(command[2]), command[3]
        if mana_needed <= information[name][1]:
            information[name][1] -= mana_needed
            print(f'{name} has successfully cast {spell} and now has {information[name][1]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell}!')
    elif 'TakeDamage' in command:
        command = command.split(' - ')
        name, damage, attacker = command[1], int(command[2]), command[3]
        information[name][0] -= damage
        if information[name][0] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {information[name][0]} HP left!')
        else:
            print(f'{name} has been killed by {attacker}!')
    elif 'Recharge' in command:
        command = command.split(' - ')
        name, amount = command[1], int(command[2])
        if information[name][1] + amount > 200:
            amount = 200 - information[name][1]
            information[name][1] = 200
            print(f'{name} recharged for {amount} MP!')
        else:
            information[name][1] += amount
            print(f'{name} recharged for {amount} MP!')
    elif 'Heal' in command:
        command = command.split(' - ')
        name, amount = command[1], int(command[2])
        if information[name][0] + amount > 100:
            amount = 100 - information[name][0]
            information[name][0] = 100
            print(f'{name} healed for {amount} HP!')
        else:
            information[name][0] += amount
            print(f'{name} healed for {amount} HP!')
    command = input()
for name, info in information.items():
    if info[0] > 0:
        print(name)
        print(f'  HP: {info[0]}\n  MP: {info[1]}')
