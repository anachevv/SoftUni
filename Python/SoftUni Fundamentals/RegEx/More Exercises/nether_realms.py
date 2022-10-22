import re

demons_names = re.findall(r"[^,\s]+", input())
info = {}
for name in range(len(demons_names)):
    health = 0
    health_regex = r"[^0-9\d\+\-\*\/\.]"
    health_pattern = re.findall(health_regex, demons_names[name])
    for match in health_pattern:
        health += ord(match)

    damage = 0
    damage_regex = r"(\-|\+)?\d+\.?\d*|\d"
    damage_pattern = re.finditer(damage_regex, demons_names[name])
    for match in damage_pattern:
        damage += float(match.group())
    if '*' in demons_names[name]:
        for i in range(demons_names[name].count('*')):
            damage *= 2
    if '/' in demons_names[name]:
        for i in range(demons_names[name].count('/')):
            damage /= 2
    info[demons_names[name]] = [health, damage]

info = dict(sorted(info.items(), key=lambda x: x[0]))
for name, stats in info.items():
    print(f"{name} - {stats[0]} health, {stats[1]:.2f} damage")
