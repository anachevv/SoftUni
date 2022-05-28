objective_height = int(input())

bar_for_jumping_height = objective_height - 30
jump_counter = 0
fails_counter = 0

while True:
    jump = int(input())
    jump_counter += 1

    if jump <= bar_for_jumping_height:
        fails_counter += 1
        if fails_counter == 3:
            print(f"Tihomir failed at {bar_for_jumping_height}cm after {jump_counter} jumps.")
            break
    else:
        if bar_for_jumping_height >= objective_height:
            print(f"Tihomir succeeded, he jumped over {objective_height}cm after {jump_counter} jumps.")
            break
        bar_for_jumping_height += 5
        fails_counter = 0
