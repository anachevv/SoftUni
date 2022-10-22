key = int(input())
n_lines = int(input())

message = ''

for line in range(n_lines):
    letter = ord(input())
    letter += key

    message += chr(letter)

print(message)
