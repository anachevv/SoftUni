year = int(input())
is_happy = False

while not is_happy:
    year += 1
    set_year = set()

    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    is_happy = len(set_year) == len(str(year))

print(year)
