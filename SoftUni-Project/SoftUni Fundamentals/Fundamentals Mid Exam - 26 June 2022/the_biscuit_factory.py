from math import floor

days = 30
number_of_biscuits_per_worker = int(input())
count_of_workers = int(input())
biscuits_of_competing_factory_per_month = int(input())
total_biscuits = 0

for day in range(1, 30 + 1):
    if day % 3 == 0:
        total_biscuits += 0.75 * (count_of_workers * number_of_biscuits_per_worker)
    else:
        total_biscuits += count_of_workers * number_of_biscuits_per_worker

    total_biscuits = floor(total_biscuits)

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > biscuits_of_competing_factory_per_month:
    percentage = (total_biscuits - biscuits_of_competing_factory_per_month) / biscuits_of_competing_factory_per_month * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif total_biscuits < biscuits_of_competing_factory_per_month:
    percentage = (biscuits_of_competing_factory_per_month - total_biscuits) / biscuits_of_competing_factory_per_month * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")
