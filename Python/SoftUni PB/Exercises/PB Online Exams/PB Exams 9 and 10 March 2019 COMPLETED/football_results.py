won_matches = 0
lost_matches = 0
tied_matches = 0

for x in range(3):
    result = input()

    if result[0] > result[2]:
        won_matches += 1
    elif result[2] > result[0]:
        lost_matches += 1
    else:
        tied_matches += 1

print(f"Team won {won_matches} games.\nTeam lost {lost_matches} games.\nDrawn games: {tied_matches}")
