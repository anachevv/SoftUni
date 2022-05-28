width_cake = int(input())
length_cake = int(input())

total_pieces = width_cake * length_cake
next_pieces = input()

while next_pieces != "STOP":

    if next_pieces == "STOP":
        break

    if next_pieces != "STOP":
        total_pieces -= int(next_pieces)

    if total_pieces < 0:
        break

    next_pieces = input()

if next_pieces == "STOP":
    print(f"{total_pieces} pieces are left.")
elif total_pieces < 0:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
