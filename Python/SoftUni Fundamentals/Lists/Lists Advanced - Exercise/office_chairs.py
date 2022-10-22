n_rooms = int(input())
total_chairs = 0
total_visitors = 0
chairs_are_enough = True
for room in range(1, n_rooms + 1):
    chairs_and_visitors = input().split()
    chairs_count = sum([1 for element in chairs_and_visitors[0]])
    total_chairs += chairs_count
    visitors = int(chairs_and_visitors[-1])
    total_visitors += visitors
    if visitors > chairs_count:
        chairs_are_enough = False
        needed_chairs = visitors - chairs_count
        print(f"{needed_chairs} more chairs needed in room {room}")

if chairs_are_enough:
    total_free_chairs = total_chairs - total_visitors
    print(f"Game On, {total_free_chairs} free chairs left")
