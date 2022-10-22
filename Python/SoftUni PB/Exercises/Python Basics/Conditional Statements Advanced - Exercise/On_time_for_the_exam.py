exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
time_difference = exam_time - arrive_time

# If the student is on time
if time_difference == 0:
    print("On time")

# If the student is up to 30 minutes earlier
elif 0 < time_difference <= 30:
    print("On time")
    print(f"{time_difference % 60} minutes before the start")\

# If the student is early 30 minutes or more
elif time_difference > 30:
    print("Early")
    if time_difference // 60 > 0:
        print(f"{time_difference // 60}:{time_difference % 60:02d} "
              f"hours before the start")
    else:
        print(f"{time_difference % 60} minutes before the start")

# If the student is late
else:
    print("Late")
    if abs(time_difference) // 60 > 0:
        print(f"{abs(time_difference) // 60 }:{abs(time_difference) % 60:02d} "
              f"hours after the start")
    else:
        print(f"{abs(time_difference) % 60} minutes after the start")
