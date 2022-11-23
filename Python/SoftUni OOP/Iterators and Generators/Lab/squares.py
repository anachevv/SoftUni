def squares(n):
    num = 0

    while num < n:
        num += 1
        yield num ** 2


print(list(squares(6)))
