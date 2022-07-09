command = input()
dct = {}

while command != "stop":
    resource = command
    quantity = int(input())

    if resource not in dct:
        dct[resource] = 0
    dct[resource] += quantity

    command = input()

for key, value in dct.items():
    print(f"{key} -> {value}")
