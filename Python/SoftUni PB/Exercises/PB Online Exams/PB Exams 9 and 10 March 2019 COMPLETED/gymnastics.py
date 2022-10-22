country = input()
instrument = input()
total_score = 0
difficulty = 0
play = 0

if instrument == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        play = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        play = 9.400
    elif country == "Italy":
        difficulty = 9.200
        play = 9.500
elif instrument == "hoop":
    if country == "Russia":
        difficulty = 9.300
        play = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        play = 9.750
    elif country == "Italy":
        difficulty = 9.450
        play = 9.350
elif instrument == "rope":
    if country == "Russia":
        difficulty = 9.600
        play = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        play = 9.400
    elif country == "Italy":
        difficulty = 9.700
        play = 9.150

total_score += difficulty + play
needed_points_percent = 20 - total_score
print(f"The team of {country} get {total_score:.3f} on {instrument}.")
print(f"{needed_points_percent / 20 * 100:.2f}%")
