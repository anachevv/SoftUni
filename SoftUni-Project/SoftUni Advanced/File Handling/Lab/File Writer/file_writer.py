def write(file):
    with open(file, 'w') as f:
        f.write("I just created my first file!")

    f.close()

    return True


file_name = "my_first_file.txt"

print(write(file_name))
