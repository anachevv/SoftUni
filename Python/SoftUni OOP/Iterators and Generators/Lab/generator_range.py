def genrange(start: int, end: int):
    num = start - 1

    while num < end:
        num += 1
        yield num


print(list(genrange(1, 10)))
