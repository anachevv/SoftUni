def read_next(*args):
    lst = []

    for el in args:
        if isinstance(el, (str, tuple, list, dict, set)):
            for x in el:
                lst.append(x)
        else:
            lst.append(el)

    for x in lst:
        yield x


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
