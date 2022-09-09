text = input()
try:
    n_times = int(input())
    result = text * n_times
    print(result)
except ValueError:
    print("Variable times must be an integer")
