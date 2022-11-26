def get_primes(lst):
    for x in lst:
        if x > 1:
            if x in (2, 3) or (x % 2 != 0 and x % 3 != 0):
                yield x
            else:
                continue


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
