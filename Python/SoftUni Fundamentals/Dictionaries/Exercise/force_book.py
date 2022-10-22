users_and_sides = {}
command = input()

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        is_present = False

        for value in users_and_sides.values():
            if force_user in value:
                is_present = True
                break
        if not is_present:
            if force_side not in users_and_sides:
                users_and_sides[force_side] = [force_user]
            else:
                users_and_sides[force_side].append(force_user)

        elif force_user not in force_side and force_user in users_and_sides.values():
            for key, value in users_and_sides.items():
                if force_user in value and key != force_side:
                    value.remove(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")

        for key, value in users_and_sides.items():
            if force_user in value:
                users_and_sides[key].remove(force_user)
                break
        if force_side not in users_and_sides:
            users_and_sides[force_side] = [force_user]
        else:
            users_and_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, value in users_and_sides.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}", end="\n! ")
        print("\n! ".join(value))
