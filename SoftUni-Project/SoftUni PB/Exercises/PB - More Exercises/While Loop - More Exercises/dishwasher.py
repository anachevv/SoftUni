detergent_bottles = int(input())

detergent_quantity = detergent_bottles * 750
detergent_per_plate = 5
detergent_per_pot = 15
filling_counter = 0
plates_counter = 0
pots_counter = 0

plates = input()

while plates != "End":

    if plates == "End":
        break

    filling_counter += 1

    if filling_counter % 3 == 0:
        detergent_quantity -= int(plates) * detergent_per_pot
        pots_counter += int(plates)
    else:
        detergent_quantity -= int(plates) * detergent_per_plate
        plates_counter += int(plates)

    if detergent_quantity < 0:
        break

    plates = input()

if detergent_quantity < 0:
    print(f"Not enough detergent, {abs(detergent_quantity)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{plates_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {detergent_quantity} ml.")
