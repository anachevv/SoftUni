def draw_shape(num):
    for row in range(1, num + 1):
        display_shape(num, row)

    for row in range(num - 1, -1, -1):
        display_shape(num, row)


def display_shape(num, row):
    print(' ' * (num - row), end='')
    for col in range(1, row + 1):
        print('* ', end='')
    print()


number = int(input())

draw_shape(number)
