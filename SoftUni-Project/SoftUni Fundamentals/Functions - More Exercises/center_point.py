from math import floor


def center_point(x_one, y_one, x_two, y_two):
    sum_of_first_list = [x_one, y_one]
    sum_of_second_list = [x_two, y_two]

    the_closest_points = sum_of_first_list if sum([abs(x_one), abs(y_one)]) < sum([abs(x_two), abs(y_two)]) else sum_of_second_list

    return f'({floor(the_closest_points[0])}, {floor(the_closest_points[1])})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(center_point(x1, y1, x2, y2))
