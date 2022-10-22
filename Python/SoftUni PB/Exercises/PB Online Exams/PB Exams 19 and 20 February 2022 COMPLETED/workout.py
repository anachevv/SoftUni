import math

n_days = int(input())
first_day_distance = float(input())

total_distance = first_day_distance

for each_day in range(n_days):
    percent_of_augmentation = int(input()) / 100
    first_day_distance *= 1 + percent_of_augmentation
    total_distance += first_day_distance

if total_distance >= 1000:
    more_distance = total_distance - 1000
    print(f"You've done a great job running {math.ceil(more_distance)} more   kilometers!")
else:
    needed_distance = 1000 - total_distance
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(needed_distance)} more kilometers")
