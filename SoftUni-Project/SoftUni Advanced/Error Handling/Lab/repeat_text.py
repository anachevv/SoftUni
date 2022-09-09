text = input()
try:
    n_times = int(input())
    result = text * 2
    print(result)
except ValueError:
    print("Variable times must be an integer")
