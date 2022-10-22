total_eggs = int(input())
buy_or_fill_eggs = input()
sold_eggs = 0

while buy_or_fill_eggs != "Close":
    bought_or_filled_eggs = int(input())

    if buy_or_fill_eggs == "Buy":
        if total_eggs < bought_or_filled_eggs:
            print(f"Not enough eggs in store!\nYou can buy only {total_eggs}.")
            break

        total_eggs -= bought_or_filled_eggs
        sold_eggs += bought_or_filled_eggs

    if buy_or_fill_eggs == "Fill":
        total_eggs += bought_or_filled_eggs

    buy_or_fill_eggs = input()

if buy_or_fill_eggs == "Close":
    print(f"Store is closed!\n{sold_eggs} eggs sold.")
