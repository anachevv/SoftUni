n = int(input())
is_all_printed = False
current_number = 1

for row in range(1, n + 1):
    for column in range(1, row + 1):

        if current_number > n:
            is_all_printed = True
            break

        print(str(current_number) + " ", end="")
        current_number += 1

    if is_all_printed:
        break

    print()
