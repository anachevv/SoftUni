from os import listdir


def traverse(file):
    extensions = sorted(set([x[x.index('.')::] for x in listdir()]))
    info = {}

    for ext in extensions:
        info[ext] = []

    for dir_file in listdir():
        for ext in info:
            if ext in dir_file:
                info[ext].append(dir_file)

    with open(file, 'w') as f:
        for ext, curr_file in info.items():
            new_line = '\n- - - '
            f.write(f"{ext}\n- - - {new_line.join(curr_file)}\n")

    f.close()

    return True


path = "report.txt"

print(traverse(path))
