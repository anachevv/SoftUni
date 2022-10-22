command = input()
coffees = 0

while command != 'END':
    keywords = ['coding', 'CODING', 'dog', 'DOG', 'cat', 'CAT', 'movie', 'MOVIE']

    if command in keywords:
        if command.islower():
            coffees += 1
        else:
            coffees += 2

    command = input()

if coffees <= 5:
    print(coffees)
elif coffees > 5:
    print('You need extra sleep')
