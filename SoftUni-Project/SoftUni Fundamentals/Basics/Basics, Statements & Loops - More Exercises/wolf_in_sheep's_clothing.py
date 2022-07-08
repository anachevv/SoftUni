user_input = input()

lst = []

for char in user_input:
    if char == 's':
        lst.append('sheep')
        continue
    elif char == 'w':
        lst.append('wolf')
        continue

lst.reverse()

if lst[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {lst.index("wolf")}! You are about to be eaten by a wolf!')
