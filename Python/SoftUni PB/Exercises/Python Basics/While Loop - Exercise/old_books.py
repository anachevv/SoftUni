book_name = input()
book_count = 0
is_book_found = False
current_book_name = input()

while current_book_name != "No More Books":
    if current_book_name == book_name:
        is_book_found = True
        print(f"You checked {book_count} books and found it.")
        break

    book_count += 1
    current_book_name = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
