n_lines = int(input())
even_numbers = set()
odd_numbers = set()

for row in range(1, n_lines + 1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)
    ascii_sum /= row
    ascii_sum = int(ascii_sum)
    even_numbers.add(ascii_sum) if ascii_sum % 2 == 0 else odd_numbers.add(ascii_sum)

even_sum = sum(even_numbers)
odd_sum = sum(odd_numbers)
if even_sum == odd_sum:
    union = even_numbers | odd_numbers
    print(", ".join(str(x) for x in union))
elif odd_sum > even_sum:
    different_values = odd_numbers.difference(even_numbers)
    print(", ".join(str(x) for x in different_values))
else:
    symmetric_difference = even_numbers.symmetric_difference(odd_numbers)
    print(", ".join(str(x) for x in symmetric_difference))
