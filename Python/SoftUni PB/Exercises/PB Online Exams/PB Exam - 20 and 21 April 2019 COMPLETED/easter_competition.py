easter_bakes = int(input())
baker_name = ""
max_points = 0
best_baker = ""

for x in range(easter_bakes):
    baker_name = input()
    evaluation = input()
    points = 0

    while evaluation != "Stop":
        points += int(evaluation)
        evaluation = input()

    print(f"{baker_name} has {points} points.")

    if max_points < points:
        max_points = points
        best_baker = baker_name
        print(f"{best_baker} is the new number 1!")

print(f"{best_baker} won competition with {max_points} points!")
