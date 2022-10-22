def reader(file):
    total_sum = 0

    with open(file, 'r') as f:
        for number in f:
            total_sum += int(number)

    f.close()

    return total_sum


path = "./numbers.txt"

print(reader(path))
