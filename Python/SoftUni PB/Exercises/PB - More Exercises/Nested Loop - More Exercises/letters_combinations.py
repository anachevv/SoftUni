start_letter = input()
end_letter = input()
insignificant_letter = input()
letter_counter = 0

for first_letter in range(ord(start_letter), ord(end_letter) + 1):
    for second_letter in range(ord(start_letter), ord(end_letter) + 1):
        for third_letter in range(ord(start_letter), ord(end_letter) + 1):
            if first_letter != ord(insignificant_letter) and second_letter != ord(insignificant_letter) and \
                    third_letter != ord(insignificant_letter):
                letter_counter += 1
                print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")

print(letter_counter)
