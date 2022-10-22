n_lines = int(input())

positives_lst = []
negatives_lst = []

for i in range(n_lines):
    number = int(input())
    if number >= 0:
        positives_lst.append(number)
    else:
        negatives_lst.append(number)

print(positives_lst)

print(negatives_lst)

print(f"Count of positives: {len(positives_lst)}\nSum of negatives: {sum(negatives_lst)}")
