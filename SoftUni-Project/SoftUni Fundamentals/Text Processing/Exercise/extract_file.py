def reverse_path(path):
    reversed_path = path[::-1]

    return reversed_path


def get_name(reversed_path):
    file_name = reversed_path[reversed_path.index('.') + 1:reversed_path.index('\\')][::-1]

    return file_name


def get_extension(path):
    file_extension = path[path.index('.') + 1::]

    return file_extension


def display_func(path):
    file_name = get_name(reverse_path(path))
    file_extension = get_extension(path)
    return f"File name: {file_name}" + f"\nFile extension: {file_extension}"


file_path = input()

print(display_func(file_path))

"""
file_path = input()

reversed_path = file_path[::-1]

file_name = reversed_path[reversed_path.index('.') + 1:reversed_path.index('\\')][::-1]
file_extension = file_path[file_path.index('.') + 1::]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
"""