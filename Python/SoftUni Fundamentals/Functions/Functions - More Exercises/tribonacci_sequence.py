def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))

    for num in res:
        if 0 in res:
            res.remove(0)

    return " ".join(str(x) for x in res)


signature = [0, 0, 1]
number = int(input()) + 2

print(tribonacci(signature, number))
