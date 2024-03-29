from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])
crafting_table = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}

presents = {}
result = 0
while materials and magic_values:
    material = materials.pop()
    magic = magic_values.popleft()

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_values.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue

    result = material * magic
    if result in crafting_table:
        present = crafting_table[result]
        if present not in presents:
            presents[present] = 1
        else:
            presents[present] += 1
        continue
    if result < 0:
        materials.append(material + magic)
    else:
        materials.append(material + 15)

if 'Doll' in presents and 'Wooden train' in presents or 'Teddy bear' in presents and 'Bicycle' in presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
for present, amount in sorted(presents.items()):
    print(f"{present}: {amount}")
