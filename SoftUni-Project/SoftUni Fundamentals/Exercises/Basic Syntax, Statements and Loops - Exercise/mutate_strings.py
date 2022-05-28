first_string = input()  # bubble gum
second_string = input()     # turtle hum
last_string = first_string

for char in range(len(first_string) + 1):
    first_part = second_string[:char + 1]
    second_part = first_string[char + 1:]
    current_string = first_part + second_part

    if current_string == last_string:
        continue
    else:
        print(current_string)
        last_string = current_string
