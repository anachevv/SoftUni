n_kilometers = int(input())
user_input = str(input())

if user_input == "day" and n_kilometers < 20:
    taxi_price = 0.7 + n_kilometers * 0.79
    print(f"{taxi_price:.2f}")
elif user_input == "day" and 20 <= n_kilometers < 100:
    bus_price = 0.09 * n_kilometers
    print(f"{bus_price:.2f}")
elif user_input == "day" and n_kilometers >= 100:
    train_price = 0.06 * n_kilometers
    print(f"{train_price:.2f}")

if user_input == "night" and n_kilometers < 20:
    taxi_price = 0.7 + n_kilometers * 0.9
    print(f"{taxi_price:.2f}")
elif user_input == "night" and 20 <= n_kilometers < 100:
    bus_price = 0.09 * n_kilometers
    print(f"{bus_price:.2f}")
elif user_input == "night" and n_kilometers >= 100:
    train_price = 0.06 * n_kilometers
    print(f"{train_price:.2f}")
