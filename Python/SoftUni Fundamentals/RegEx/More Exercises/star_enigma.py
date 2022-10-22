import re

n_messages = int(input())
regex = r"(\@([A-Z][a-z]+)[^\:@\-!>?]*\:(\d+)[^\:@\-!>?]*\!([AD])![^\:@\-!>\d?]*\-\>(\d+))"
attacked_planets = 0
destroyed_planets = 0
attacked = []
destroyed = []
for _ in range(n_messages):
    message = input()
    count = 0
    letters = [letter for letter in 'star']
    decrypted_message = ""
    for char in message.lower():
        if char in letters:
            count += 1
    for char in message:
        decrypted_message += chr(ord(char) - count)
    search_pattern = re.search(regex, decrypted_message)
    if search_pattern:
        planet = search_pattern.group(2)
        population = search_pattern.group(3)
        attack_type = search_pattern.group(4)
        soldier_count = search_pattern.group(5)
        if attack_type == 'A':
            if planet not in attacked:
                attacked_planets += 1
                attacked.append(planet)
        elif attack_type == 'D':
            if planet not in destroyed:
                destroyed_planets += 1
                destroyed.append(planet)

attacked = sorted(attacked)
destroyed = sorted(destroyed)
print("Attacked planets: {}".format(attacked_planets))
for planet in attacked:
    print(f"-> {planet}")
print("Destroyed planets: {}".format(destroyed_planets))
for planet in destroyed:
    print(f"-> {planet}")
