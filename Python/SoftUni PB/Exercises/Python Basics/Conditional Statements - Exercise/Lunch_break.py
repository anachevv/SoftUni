import math

series = input()
series_duration = int(input())
break_duration = int(input())

lunch_duration = 1/8 * break_duration
time_for_rest = 1/4 * break_duration

remaining_time_for_series = break_duration - \
                            lunch_duration - time_for_rest
needed_time = abs(remaining_time_for_series - series_duration)
if remaining_time_for_series >= series_duration:
    print(f"You have enough time to watch {series} and left with {math.ceil(needed_time)} "
          f"minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(needed_time)} more minutes.")
