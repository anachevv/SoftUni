sequence_of_numbers = input().split()
happiness_improvement_factor = int(input())

lst = [int(number) * happiness_improvement_factor for number in sequence_of_numbers]

happy_employees = len(list((filter(lambda x: x >= sum(lst) / len(lst), lst))))

if happy_employees >= len(lst) / 2:
    print(f"Score: {happy_employees}/{len(lst)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(lst)}. Employees are not happy!")
