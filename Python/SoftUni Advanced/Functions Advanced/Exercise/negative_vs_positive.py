def compare_numbers(nums):
    def calculate_sum():
        positive_sum = sum([x for x in nums if x > 0])
        negative_sum = sum([y for y in nums if y < 0])

        return negative_sum, positive_sum

    def display_message():
        negative_sum = calculate_sum()[0]
        positive_sum = calculate_sum()[1]
        result = str(negative_sum) + '\n' + str(positive_sum)
        if abs(negative_sum) > abs(positive_sum):
           result += "\nThe negatives are stronger than the positives"
        else:
           result += "\nThe positives are stronger than the negatives"
        
        return result

    return display_message()


numbers = [int(x) for x in input().split()]

print(compare_numbers(numbers))
