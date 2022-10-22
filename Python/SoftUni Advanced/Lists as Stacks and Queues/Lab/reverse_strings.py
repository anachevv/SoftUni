# Best practice

# # user_input = input()
# # reversed_input = user_input[::-1]
# print(reversed_input)


# Using Stacks

user_input = input()
stack = [char for char in user_input]
reversed_string = ""
while stack:
    reversed_string += stack.pop()
print(reversed_string)
