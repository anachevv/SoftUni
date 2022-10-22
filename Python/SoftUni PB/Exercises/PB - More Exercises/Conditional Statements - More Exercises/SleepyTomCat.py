days_off = int(input())
days_off_play = days_off * 127
workday = (365 - days_off) * 63
play_time = days_off_play + workday
play_norm_time = 30000

if play_time > play_norm_time:
    time_difference = play_time - play_norm_time
    hours = time_difference // 60
    minutes = time_difference - (hours * 60)
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

elif play_time < play_norm_time:
    time_difference = play_norm_time - play_time
    hours = time_difference // 60
    minutes = time_difference - (hours * 60)
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
