def fill_the_box(height, length, width, *args):
    volume_to_fill = height * length * width

    for number in args:
        if number == 'Finish':
            break
        volume_to_fill -= number

    if volume_to_fill > 0:
        return f"There is free space in the box. You could put {volume_to_fill} more cubes."

    return f"No more free space! You have {abs(volume_to_fill)} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

