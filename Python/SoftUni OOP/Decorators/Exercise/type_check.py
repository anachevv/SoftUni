def type_check(input_type):
    def decorator(function):
        def wrapper(param):
            if input_type != type(param):
                return "Bad Type"
            return function(param)
        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
