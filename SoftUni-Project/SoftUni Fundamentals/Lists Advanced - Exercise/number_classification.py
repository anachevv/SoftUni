lst = [x for x in input().split(', ')]
positive_numbers = [x for x in lst if int(x) >= 0]
negative_numbers = [y for y in lst if int(y) < 0]
even_numbers = [z for z in lst if int(z) % 2 == 0]
odd_numbers = [q for q in lst if int(q) % 2 != 0]

print(f"Positive: {', '.join(x for x in positive_numbers)}")
print(f"Negative: {', '.join(x for x in negative_numbers)}")
print(f"Even: {', '.join(x for x in even_numbers)}")
print(f"Odd: {', '.join(x for x in odd_numbers)}")
