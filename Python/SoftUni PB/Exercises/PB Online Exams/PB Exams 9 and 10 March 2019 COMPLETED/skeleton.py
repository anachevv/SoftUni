import math

minutes = int(input())
seconds = int(input())
length = float(input())
seconds_per_100m = int(input())

total_time = minutes * 60 + seconds
delay = length / 120
total_delay = delay * 2.5
player_time = length / 100 * seconds_per_100m - total_delay

if player_time <= total_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {player_time:.3f}.")
else:
    needed_time = player_time - total_time
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")
