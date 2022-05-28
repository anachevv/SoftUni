t_shirt_price = float(input())
needed_sum_for_ball = float(input())
ball_is_earned = False

shorts_price = 0.75 * t_shirt_price
socks_price = 0.2 * shorts_price
football_sneakers_price = 2 * (t_shirt_price + shorts_price)
discount = 0.15

price = t_shirt_price + shorts_price + socks_price + football_sneakers_price
total_price = price - (discount * price)

if total_price >= needed_sum_for_ball:
    ball_is_earned = True

if ball_is_earned:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    needed_sum = needed_sum_for_ball - total_price
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_sum:.2f} lv. more.")
