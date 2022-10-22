from string import punctuation


def numbers(file):
    result = ""

    with open(file, 'r') as f:
        line_number = 0

        for curr_line in f:
            words = 0
            marks = 0
            line_number += 1
            line = f"Line {line_number}"

            for el in curr_line:
                if el.isalpha():
                    words += 1
                elif el in punctuation:
                    marks += 1

            result += f"{line}: {curr_line.strip()} ({words}) ({marks})" + '\n'

    return result


path = "line-numbers.txt"

print(numbers(path))


def write_result(new_file):
    result = numbers(path)

    with open(new_file, 'w') as f:
        f.write(result)

    f.close()


new_path = "../File Manipulator/line-numbers-result-file.txt"

write_result(new_path)
