chicken_menu = 10.35
fish_menu = 12.4
vegetarian_menu = 8.15
delivery_bill = 2.5
chicken_menu_number = int(input())
fish_menu_number = int(input())
vegetarian_menu_number = int(input())
price = (chicken_menu_number * 10.35) + (fish_menu_number * 12.4) + (vegetarian_menu_number * 8.15)
dessert = (20/100 * price)
total = price + dessert + 2.5
print(total)
