import re

regex = r"(\%([A-Z][a-z]+)\%[^$%.|?]*\<(\w+)\>[^$%.|?]*\|(\d+)\|[^\d$%.|?]*[A-Za-z]*(\d+\.?\d*)\$)"
command = input()
total_sum = 0
while command != "end of shift":
    search_pattern = re.search(regex, command)
    if search_pattern:
        customer, product, count, price = search_pattern.group(2), search_pattern.group(3), int(search_pattern.group(4)), float(search_pattern.group(5))
        total_sum += count * price
        print(f"{customer}: {product} - {count * price:.2f}")
    command = input()
print(f"Total income: {total_sum:.2f}")
