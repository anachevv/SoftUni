n = int(input())
heartstone = 0
fortnite = 0
overwatch = 0
others = 0

for x in range(n):
    game_name = input()

    if game_name == "Hearthstone":
        heartstone += 1
    elif game_name == "Fornite":
        fortnite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {heartstone / n * 100:.2f}%\n"
      f"Fornite - {fortnite / n * 100:.2f}%\n"
      f"Overwatch - {overwatch / n * 100:.2f}%\n"
      f"Others - {others / n * 100:.2f}%\n")
