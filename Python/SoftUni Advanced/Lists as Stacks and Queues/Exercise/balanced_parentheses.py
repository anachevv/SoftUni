user_input = input()
stack = []
valid = True

for char in user_input:
    if char in '{[(':
        stack.append(char)
    elif not stack:
        valid = False
        break
    else:
        last_opening_bracket = stack.pop()
        if last_opening_bracket + char not in '{}[]()':
            valid = False
            break

if valid and not stack:
    print("YES")
else:
    print("NO")
