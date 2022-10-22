dancers = int(input())
points = float(input())
season = input()
place = input()

prize = 0
charity_sum = 0

if place == "Bulgaria":
    prize = points * dancers
    if season == "summer":
        prize -= 0.05 * prize
    elif season == "winter":
        prize -= 0.08 * prize

elif place == "Abroad":
    prize = dancers * points + (0.5 * dancers * points)
    if season == "summer":
        prize -= 0.1 * prize
    elif season == "winter":
        prize -= 0.15 * prize

charity_sum = 0.75 * prize
prize -= charity_sum
prize /= dancers

print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {prize:.2f}")
