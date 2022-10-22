command = input()
needed_steps = 10000
target_reached = False
total_steps = 0

while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= needed_steps:
        break

    command = input()

if command == "Going home":
    steps = int(input())
    total_steps += steps

if total_steps >= needed_steps:
    target_reached = True
difference = abs(total_steps - needed_steps)

if target_reached:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
