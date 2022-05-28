command = input()

goals = 0
best_player = ""

while command != "END":

    player_name = command
    current_goals = int(input())

    if current_goals > goals:
        goals = current_goals
        best_player = player_name

    if goals >= 10:
        break

    command = input()

if goals >= 3:
    print(f"{best_player} is the best player!")
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!")
    print(f"He has scored {goals} goals.")
