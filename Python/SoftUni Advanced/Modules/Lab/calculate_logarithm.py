from math import log

number = int(input())
log_base = input()
if log_base == "natural":
    number_log = log(number)
else:
    log_base = int(log_base)
    number_log = log(number, log_base)
print(f"{number_log:.2f}")
