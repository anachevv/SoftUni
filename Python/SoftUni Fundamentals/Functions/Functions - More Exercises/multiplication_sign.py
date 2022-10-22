def multiplication_sign(first_num, second_num, third_num):
    result = ""
    lst = [first_num, second_num, third_num]
    negative_count = len([number for number in lst if number < 0])
    if 0 in lst:
        result = "zero"
    elif negative_count % 2 != 0 and 0 not in lst:
        result = "negative"
    elif negative_count % 2 == 0 and 0 not in lst:
        result = "positive"

    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_sign(first_number, second_number, third_number))
