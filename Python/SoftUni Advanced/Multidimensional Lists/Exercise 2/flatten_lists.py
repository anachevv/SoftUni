def flatten(nums):
    nums = [int(x) for lst in nums[::-1] for x in lst]
    result = ' '.join(str(x) for x in nums)

    return result


numbers = [y.strip().split() for y in input().split('|')]

print(flatten(numbers))
