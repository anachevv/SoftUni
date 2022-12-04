def tags(tag):
    def decorator(function):
        def wrapper(*args):
            open_tag = f"<{tag}>"
            close_tag = f"</{tag}>"
            result = f"{open_tag}{function(*args)}{close_tag}"
            return result
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
