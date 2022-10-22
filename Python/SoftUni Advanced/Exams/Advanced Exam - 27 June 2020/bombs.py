from collections import deque


def mixing(bomb_effects, bomb_casings):
    bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
    pouch_is_filled = False
    result = ""

    while bomb_effects and bomb_casings:
        if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
            pouch_is_filled = True
            result += "Bene! You have successfully filled the bomb pouch!\n"
            break
        effect = bomb_effects.popleft()
        casing = bomb_casings.pop()
        curr_sum = effect + casing

        if curr_sum == 40:
            bombs["Datura Bombs"] += 1
            continue
        elif curr_sum == 60:
            bombs["Cherry Bombs"] += 1
            continue
        elif curr_sum == 120:
            bombs["Smoke Decoy Bombs"] += 1
            continue
        else:
            bomb_effects.appendleft(effect)
            bomb_casings.append(casing - 5)

    if not pouch_is_filled:
        result += "You don't have enough materials to fill the bomb pouch.\n"

    if bomb_effects:
        result += f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}\n"
    else:
        result += "Bomb Effects: empty\n"

    if bomb_casings:
        result += f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}\n"
    else:
        result += "Bomb Casings: empty\n"

    bombs = sorted(bombs.items(), key=lambda x: (x[0]))

    for info in bombs:
        effect = info[0]
        casing = info[1]
        result += f"{effect}: {casing}\n"

    return result


bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(y) for y in input().split(', ')]


print(mixing(bomb_effects, bomb_casings))

