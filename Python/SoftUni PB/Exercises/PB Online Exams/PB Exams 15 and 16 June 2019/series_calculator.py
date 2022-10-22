import math

series_name = input()
seasons = int(input())
episodes = int(input())
time_episode_no_ads = float(input())
ads_time = 0.2 * time_episode_no_ads
episode_time = time_episode_no_ads + ads_time
total_time = episode_time * episodes * seasons + (seasons * 10)

print(f"Total time needed to watch the {series_name} series is {math.floor(total_time)} minutes.")
