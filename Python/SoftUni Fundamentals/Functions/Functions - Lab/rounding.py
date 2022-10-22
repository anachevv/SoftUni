def rounding(string=input()):

    string = string.split()
    lst = [round(float(x)) for x in string]

    return lst


print(rounding())
