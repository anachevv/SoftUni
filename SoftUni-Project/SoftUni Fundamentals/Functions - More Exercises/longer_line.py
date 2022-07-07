from math import floor


def center_point(x_one, y_one, x_two, y_two, x_three, y_three, x_four, y_four):
    first_list = [x_one, y_one, x_two, y_two]
    second_list = [x_three, y_three, x_four, y_four]

    first_sum = sum(abs(x) for x in first_list)
    second_sum = sum(abs(y) for y in second_list)

    the_closest_points = first_list if first_sum > second_sum else second_list if second_sum > first_sum else first_list

    if sum([abs(the_closest_points[0]), abs(the_closest_points[1])]) < sum([abs(the_closest_points[2]), abs(the_closest_points[3])]):
        first_pair = [str(floor(the_closest_points[0])), str(floor(the_closest_points[1]))]
        second_pair = [str(floor(the_closest_points[2])), str(floor(the_closest_points[3]))]
    elif sum([abs(the_closest_points[0]), abs(the_closest_points[1])]) > sum([abs(the_closest_points[2]), abs(the_closest_points[3])]):
        first_pair = [str(floor(the_closest_points[2])), str(floor(the_closest_points[3]))]
        second_pair = [str(floor(the_closest_points[0])), str(floor(the_closest_points[1]))]
    else:
        first_pair = [str(floor(the_closest_points[0])), str(floor(the_closest_points[1]))]
        second_pair = [str(floor(the_closest_points[2])), str(floor(the_closest_points[3]))]

    return f'({", ".join(first_pair)})({", ".join(second_pair)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(center_point(x1, y1, x2, y2, x3, y3, x4, y4))
