import re

command = input()
regex = r">>([A-za-z]+)<<(\d+\.?\d*)!(\d+)"
total_price = 0
furniture_list = []
while command != 'Purchase':
    search_pattern = re.search(regex, command)
    if search_pattern is not None:
        furniture = search_pattern.group(1)
        price = float(search_pattern.group(2))
        quantity = int(search_pattern.group(3))
        total_price += price * quantity
        furniture_list.append(furniture)
    command = input()
print("Bought furniture:")
for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_price:.2f}')
