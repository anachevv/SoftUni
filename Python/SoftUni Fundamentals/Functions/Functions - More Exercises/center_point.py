from math import floor


def center_point(x_one, y_one, x_two, y_two):
    first_list = [x_one, y_one]
    second_list = [x_two, y_two]

    first_sum = sum([abs(x_one), abs(y_one)])
    second_sum = sum([abs(x_two), abs(y_two)])

    the_closest_points = first_list if first_sum < second_sum else second_list if second_sum < first_sum else first_list

    return f'({floor(the_closest_points[0])}, {floor(the_closest_points[1])})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(center_point(x1, y1, x2, y2))
