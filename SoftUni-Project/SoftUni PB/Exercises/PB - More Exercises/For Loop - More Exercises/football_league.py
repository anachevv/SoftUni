stadium = int(input())
total_fans = int(input())
first_team_a = 0
first_team_b = 0
second_team_v = 0
second_team_g = 0

for x in range(total_fans):
    sector = input()

    if sector == "A":
        first_team_a += 1
    elif sector == "B":
        first_team_b += 1
    elif sector == "V":
        second_team_v += 1
    elif sector == "G":
        second_team_g += 1

print(f"{first_team_a / (first_team_a + first_team_b + second_team_v + second_team_g) * 100:.2f}%")
print(f"{first_team_b / (first_team_a + first_team_b + second_team_v + second_team_g) * 100:.2f}%")
print(f"{second_team_v / (first_team_a + first_team_b + second_team_v + second_team_g) * 100:.2f}%")
print(f"{second_team_g / (first_team_a + first_team_b + second_team_v + second_team_g) * 100:.2f}%")
print(f"{(first_team_a + first_team_b + second_team_v + second_team_g) / stadium * 100:.2f}%")
