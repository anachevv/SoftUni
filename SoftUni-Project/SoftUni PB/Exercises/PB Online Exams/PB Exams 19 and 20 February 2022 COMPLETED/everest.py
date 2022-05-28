command = input()
level_of_climbing = 5364
overnights_counter = 1

while command != "END":

    wants_to_spend_the_night = command

    if wants_to_spend_the_night == "Yes":
        overnights_counter += 1

    if overnights_counter > 5:
        break

    climbed_meters = int(input())
    level_of_climbing += climbed_meters

    if level_of_climbing >= 8848:
        break

    command = input()

if command == "END" or overnights_counter > 5:
    print("Failed!")
    print(f"{level_of_climbing}")
if level_of_climbing >= 8848 and overnights_counter <= 5:
    print(f"Goal reached for {overnights_counter} days!")
