x_house_height = float(input())
y_side_wall_length = float(input())
h_triangle_side_height = float(input())

# House

area_side_walls = x_house_height * y_side_wall_length * 2
area_windows = 1.5 * 1.5 * 2
total_area_sides = area_side_walls - area_windows
area_door = 1.2 * 2
front_and_back_walls = 2 * (x_house_height * x_house_height) - area_door
total_area = total_area_sides + front_and_back_walls
green_paint = total_area / 3.4

# Roof

roof_rectangles = 2 * (x_house_height * y_side_wall_length)
roof_triangles = 2 * (x_house_height * h_triangle_side_height / 2)
area_roof = roof_rectangles + roof_triangles
red_paint = area_roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
