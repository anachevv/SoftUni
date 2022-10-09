from os import listdir, remove


def delete(file):
    file_exists = file in listdir()

    try:
        remove(file)

    except FileNotFoundError:
        if not file_exists:
            return "No such file!"
        return "File already deleted!"


file = "my_first_file.txt"

print(delete(file))
