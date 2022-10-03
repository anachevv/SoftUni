def display_result(path):
    file = open(path, 'r')
    total_sum = 0
    
    for number in file:
        total_sum += int(number)


    return total_sum


path = "./numbers.txt"

print(display_result(path))
