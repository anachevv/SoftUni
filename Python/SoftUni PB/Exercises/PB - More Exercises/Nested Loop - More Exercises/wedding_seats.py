last_sector = input()
first_sector_rows = int(input())
odd_row_seats = int(input())

start_sector = 65
seats_counter = 0
start_seat = 97

for sector in range(start_sector, ord(last_sector) + 1):
    for row in range(1, first_sector_rows + 1):

        if row % 2 != 0:
            for seats in range(start_seat, (start_seat + odd_row_seats)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                seats_counter += 1
        elif row % 2 == 0:
            for seats in range(start_seat, (start_seat + odd_row_seats + 2)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                seats_counter += 1

    if first_sector_rows + 1 > first_sector_rows:
        first_sector_rows += 1

print(seats_counter)
