n_lines = int(input())
elements = set()
for _ in range(n_lines):
    element = input()
    if element.count(' ') >= 1:
        element = element.split()
        for x in element:
            elements.add(x)
    else:
        elements.add(element)
print("\n".join(elements))
