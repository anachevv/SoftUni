n_guests = int(input())
info = []
for _ in range(n_guests):
    guest = input()
    info.append(guest)

command = input()
while command != 'END':
    participant = command
    if participant in info:
        info.remove(participant)
    command = input()
info = sorted(set(info))
print(len(info))
print('\n'.join(info))
