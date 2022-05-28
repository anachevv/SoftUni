n_numbers = int(input())

even_list = []
even_total_sum = 0
even_min_sum = 0
even_max_sum = 0

odd_list = []
odd_total_sum = 0
odd_min_sum = 0
odd_max_sum = 0

number = 0

for x in range(1, n_numbers + 1):
    number = float(input())

    if x % 2 == 0:
        even_total_sum += number
        even_list.append(number)
        even_list.sort()
    else:
        odd_total_sum += number
        odd_list.append(number)
        odd_list.sort()

if n_numbers == 1:
    if number % 2 == 0:
        print(f"OddSum=0.00,")
        print(f"OddMin=No,")
        print(f"OddMax=No,")
        print(f"EvenSum={number:.2f},")
        print(f"EvenMin={number:.2f},")
        print(f"EvenMax={number:.2f}")
    else:
        print(f"OddSum={number:.2f},")
        print(f"OddMin={number:.2f},")
        print(f"OddMax={number:.2f},")
        print(f"EvenSum=0.00,")
        print(f"EvenMin=No,")
        print(f"EvenMax=No")

elif n_numbers == 0:
    print(f"OddSum=0.00,")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
    print(f"EvenSum={number:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")

else:
    print(f"OddSum={odd_total_sum:.2f},")
    if number == min(odd_list):
        print(f"OddMin={min(odd_list):.2f},")
    else:
        print(f"OddMin={min(odd_list):.2f},")
    if number == max(odd_list):
        print(f"OddMax={max(odd_list):.2f},")
    else:
        print(f"OddMax={max(odd_list):.2f},")

    print(f"EvenSum={even_total_sum:.2f},")
    if number == min(even_list):
        print(f"EvenMin={min(even_list):.2f},")
    else:
        print(f"EvenMin={min(even_list):.2f},")
    if number == max(even_list):
        print(f"EvenMax={max(even_list):.2f}")
    else:
        print(f"EvenMax={max(even_list):.2f}")
