command = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places = free_places

    while free_places > 0:
        current_ticket_type = input()

        if current_ticket_type == "End":
            break

        elif current_ticket_type == "student":
            student_tickets += 1
        elif current_ticket_type == "standard":
            standard_tickets += 1
        elif current_ticket_type == "kid":
            kid_tickets += 1

        free_places -= 1
        sold_tickets += 1
        total_tickets += 1
    full_cinema = sold_tickets / total_places * 100
    print(f"{movie_name} - {full_cinema:.2f}% full.")

    command = input()

student_tickets_percent = student_tickets / total_tickets * 100
standard_tickets_percent = standard_tickets / total_tickets * 100
kid_tickets_percent = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.")
print(f"{kid_tickets_percent:.2f}% kids tickets.")
