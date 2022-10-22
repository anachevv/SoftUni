first_player_name = input()
first_player_points = 0

second_player_name = input()
second_player_points = 0

command = input()

is_number_wars = False
winner = ""
winner_points = 0

while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())

    if first_player_card > second_player_card:
        first_player_points += (first_player_card - second_player_card)

    elif second_player_card > first_player_card:
        second_player_points += (second_player_card - first_player_card)

    elif first_player_card == second_player_card:
        is_number_wars = True
        first_player_another_card = int(input())
        second_player_another_card = int(input())
        if first_player_another_card > second_player_another_card:
            winner = first_player_name
            winner_points = first_player_points
            break
        elif second_player_another_card > first_player_another_card:
            winner = second_player_name
            winner_points = second_player_points
            break

    command = input()

if command == "End of game":
    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")
if is_number_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
