from collections import deque


def get_colors(colors_substrings):
    main_colors = ['red', 'yellow', 'blue']
    secondary_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}
    colors = []

    while colors_substrings:
        left_part = colors_substrings.popleft()
        right_part = colors_substrings.pop() if colors_substrings else ''
        color = left_part + right_part

        if color in main_colors or color in secondary_colors:
            colors.append(color)
            continue

        color = right_part + left_part

        if color in main_colors or color in secondary_colors:
            colors.append(color)
            continue

        left_part, right_part = left_part[:-1], right_part[:-1]

        if left_part:
            colors_substrings.insert(len(colors_substrings) // 2, left_part)
        if right_part:
            colors_substrings.insert(len(colors_substrings) // 2, right_part)

    for key in secondary_colors:
        if key in colors:
            if secondary_colors[key][0] not in colors or secondary_colors[key][1] not in colors:
                colors.remove(key)

    return colors


colors_substrings = deque(input().split())

print(get_colors(colors_substrings))
