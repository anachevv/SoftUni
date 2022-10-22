def repeat_string(string=input(),n_counter=int(input())):

    new_string = "".join(string * n_counter)

    return new_string


print(repeat_string())
