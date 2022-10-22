from collections import deque


def get_details():
    robots_info = {}
    robots_details = input().split(';')
    for details in robots_details:
        details = details.split('-')
        name, time = details[0], int(details[1])
        robots_info[name] = time
    return robots_info


def get_time(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds

# Robot info
robots_info = get_details()
available_robots = [robot for robot in robots_info]
working_robots = {}

# Time info
start_time = [int(x) for x in input().split(':')]
total_time = get_time(start_time[0], start_time[1], start_time[2])


def get_products():
    products = deque()
    while True:
        line = input()
        if line == 'End':
            break
        products.append(line)
    return products


def display_time(total_time):
    hours = total_time // 3600
    minutes = total_time % 3600 // 60
    seconds = total_time % 3600 % 60
    str_format = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return str_format


products = get_products()

while products:
    total_time = (total_time + 1) % (24 * 60 * 60)

    for robot in [k for k in working_robots]:
        working_robots[robot] -= 1
        if working_robots[robot] <= 0:
            del working_robots[robot]

    for robot in available_robots:
        if robot not in working_robots:
            print(f"{robot} - {products.popleft()} [{display_time(total_time)}]")
            working_robots[robot] = robots_info[robot]
            break
    else:
        products.append(products.popleft())
