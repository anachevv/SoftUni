info = input().split()
first_length, second_length = int(info[0]), int(info[1])
n_numbers = first_length + second_length
first_collection = set()
second_collection = set()
for i in range(n_numbers):
    number = int(input())
    if i < first_length:
        first_collection.add(number)
    else:
        second_collection.add(number)
print("\n".join(str(x) for x in first_collection & second_collection))
