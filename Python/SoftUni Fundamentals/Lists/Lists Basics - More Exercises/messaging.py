sequence_of_numbers = input().split(' ')
string = input()
message = ''
string_list = [char for char in string]

for chars in sequence_of_numbers:
    sum_of_numbers = 0

    for ch in chars:
        sum_of_numbers += int(ch)
        if sum_of_numbers > len(string):
            sum_of_numbers -= len(string)

    message += string_list[sum_of_numbers]
    string_list.pop(sum_of_numbers)

print(message)
