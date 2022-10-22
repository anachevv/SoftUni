# a = int(input())
# b = int(input())
#
# print(f'Before:\na = {a}\nb = {b}')
#
# a, b = b, a
#
# print(f'After:\na = {a}\nb = {b}')


a = int(input())
b = int(input())

tmp = a
a = b
b = tmp

print(f'Before:\na = {tmp}\nb = {a}\nAfter:\na = {a}\nb = {b}')
