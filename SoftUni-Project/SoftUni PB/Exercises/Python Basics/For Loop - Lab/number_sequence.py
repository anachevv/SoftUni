n = int(input())
number = []

for x in range(0, n):
    number.append(int(input()))

print(f"Max number: {max(number)}")
print(f"Min number: {min(number)}")
