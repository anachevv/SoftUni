string = input()
hidden_message = ""

num_lst = [int(element) for element in string if element.isdigit()]
take_lst = [x for x in num_lst if num_lst.index(x) % 2 == 0]
skip_lst = [y for y in num_lst if num_lst.index(y) % 2 != 0]

alpha_lst = []
