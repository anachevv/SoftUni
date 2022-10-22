def grocery_store(**kwargs):
    result = ""
    receipt = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for product in receipt:
        result += product[0] + ': ' + str(product[1]) + '\n'
    
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

