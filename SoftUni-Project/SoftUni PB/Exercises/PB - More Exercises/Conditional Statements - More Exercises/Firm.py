import math

necessary_hours = int(input())
days = int(input())
extra_workers = int(input())

project_hours = (days - 0.1 * days) * 8
extra_work = extra_workers * 2 * days
total_hours = math.floor(project_hours + extra_work)

if total_hours >= necessary_hours:
    remaining_time = total_hours - necessary_hours
    print(f"Yes!{remaining_time} hours left.")
elif total_hours < necessary_hours:
    insufficient_time = necessary_hours - total_hours
    print(f"Not enough time!{insufficient_time} hours needed.")
