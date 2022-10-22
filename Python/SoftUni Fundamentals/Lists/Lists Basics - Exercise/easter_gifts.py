names_of_the_gifts = input().split()
command = input()

while command != 'No Money':

    if 'OutOfStock' in command:
        command, gift = command.split()

        for current_gift in range(len(names_of_the_gifts)):
            if names_of_the_gifts[current_gift] == gift:
                names_of_the_gifts[current_gift] = 'None'
    elif 'Required' in command:
        command, gift, index = command.split()
        index = int(index)

        if 0 < index < len(names_of_the_gifts):
            names_of_the_gifts[index] = gift
    elif 'JustInCase' in command:
        command, gift = command.split()
        names_of_the_gifts[-1] = gift

    command = input()

for gift in range(len(names_of_the_gifts)):
    if 'None' in names_of_the_gifts:
        names_of_the_gifts.remove('None')

string_of_the_gifts = " ".join(names_of_the_gifts)

print(string_of_the_gifts)
