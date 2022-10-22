import math

easter_bread = int(input())
needed_sugar = 0
needed_flour = 0
sugar_list = []
flour_list = []
total_needed_sugar = 0
total_needed_flour = 0

for x in range(0, easter_bread):
    needed_sugar = int(input())
    needed_flour = int(input())
    total_needed_sugar += needed_sugar
    total_needed_flour += needed_flour

    sugar_list.append(needed_sugar)
    flour_list.append(needed_flour)

sugar_packets = math.ceil(total_needed_sugar / 950)
flour_packets = math.ceil(total_needed_flour / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max(flour_list)} grams, max used sugar is {max(sugar_list)} grams.")
