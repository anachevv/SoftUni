def loading_bar(num):
    percent_count = int(num / 10)
    dots_count = 10 - percent_count

    if num == 100:
        return f"{num}% Complete!\n[%%%%%%%%%%]"
    elif num == 0:
        return f"{num}% [{dots_count * '.'}]\nStill loading..."
    return f"{num}% [{percent_count * '%'}{dots_count * '.'}]\nStill loading..."


number = int(input())

print(loading_bar(number))
