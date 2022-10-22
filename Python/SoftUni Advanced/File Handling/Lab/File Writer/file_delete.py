from os import listdir, remove


def delete(file):
    if file in listdir():
        remove(file)
    else:
        print("File already deleted!")

    return True


path = "./my_first_file.txt"

print(delete(path))
