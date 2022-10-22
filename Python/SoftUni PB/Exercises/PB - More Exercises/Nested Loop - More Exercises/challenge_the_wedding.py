men_clients = int(input())
women_clients = int(input())
max_tables = int(input())

tables_taken = 0

for m in range(1, men_clients + 1):
    for w in range(1, women_clients + 1):
        tables_taken += 1

        if tables_taken > max_tables:
            break
        else:
            print(f"({m} <-> {w})", end=" ")
