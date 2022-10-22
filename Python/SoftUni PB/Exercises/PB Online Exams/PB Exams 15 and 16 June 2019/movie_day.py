taking_photos_time = int(input())
number_of_scenes = int(input())
scene_time = int(input())

terrain_preparing = 0.15 * taking_photos_time
total_needed_time = number_of_scenes * scene_time + terrain_preparing

difference = abs(taking_photos_time - total_needed_time)

if taking_photos_time >= total_needed_time:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")
