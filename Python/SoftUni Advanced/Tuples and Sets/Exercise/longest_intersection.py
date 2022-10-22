n_lines = int(input())
longest_intersection = set()
for _ in range(n_lines):
    info = [x.split(',') for x in input().split('-')]
    first_start, first_end = int(info[0][0]), int(info[0][1])
    second_start, second_end = int(info[1][0]), int(info[1][1])
    first_collection = set(x for x in range(first_start, first_end + 1))
    second_collection = set(y for y in range(second_start, second_end + 1))
    current_intersection = first_collection & second_collection
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")
