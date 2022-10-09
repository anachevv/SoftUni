from os import listdir, remove


def create(file_name):
    file = open(f"./{file_name}", 'w')
    file.close()


def add(file, content):
    with open(file, 'a') as f:
        f.write(content + '\n')


def replace(file, old, new):
    if file not in listdir():
        print("An error occurred")
    else:
        with open(file, 'r+') as f:
            new_content = f.read().replace(old, new)
            f.seek(0)
            f.truncate()
            f.write(new_content)


def delete(file):
    if file not in listdir():
        print("An error occurred")
    else:
        remove(file)


command = input()

while command != "End":
    command = command.split('-')

    if "Create" in command:
        file_name = command[1]
        create(file_name)

    elif "Add" in command:
        file_name, content = command[1], command[2]
        add(file_name, content)

    elif "Replace" in command:
        file_name, old_string, new_string = command[1], command[2], command[3]
        replace(file_name, old_string, new_string)

    elif "Delete" in command:
        file_name = command[1]
        delete(file_name)

    command = input()
