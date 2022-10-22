c_count = 0
o_count = 0
n_count = 0
secret_word = ""

while True:

    user_input = input()

    if user_input == "End":
        break
    if user_input == "c" and c_count == 0:
        c_count += 1
    elif user_input == "o" and o_count == 0:
        o_count += 1
    elif user_input == "n" and n_count == 0:
        n_count += 1
    else:
        if user_input.isalpha():
            secret_word += user_input

    if c_count == 1 and o_count == 1 and n_count == 1:
        print(f"{secret_word} ", end="")

        secret_word = ""
        c_count = 0
        o_count = 0
        n_count = 0
