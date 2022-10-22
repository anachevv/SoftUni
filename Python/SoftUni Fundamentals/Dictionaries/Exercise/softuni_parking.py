n_commands = int(input())
validated_users = {}
unregistered_users = []

for _ in range(n_commands):
    command = input().split()

    if 'register' in command:
        name, plate = command[1], command[2]
        if name not in validated_users:
            validated_users[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    elif 'unregister' in command:
        name = command[1]
        if name in validated_users:
            unregistered_users.append(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, plate in validated_users.items():
    if name not in unregistered_users:
        print(f"{name} => {plate}")
