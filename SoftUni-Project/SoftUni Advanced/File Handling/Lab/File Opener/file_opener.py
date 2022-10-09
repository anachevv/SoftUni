def open_file(path):
    try:
        file = open(path, 'r')
        return "File found"
    except:
        return "File not found"


path = "./text.txt"

print(open_file(path))
