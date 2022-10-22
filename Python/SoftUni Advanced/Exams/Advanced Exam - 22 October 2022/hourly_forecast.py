def forecast(*args):
    info = {}
    for t in args:
        location = t[0]
        weather = t[1]
        info[location] = weather

    info = dict(sorted(info.items(), key=lambda x: (x[0])))
    info = sorted(info.items(), key=lambda x: ((x[1] == 'Sunny'), (x[1] == 'Cloudy'), (x[1] == 'Rainy')), reverse=True)
    result = ""

    for location, weather in info:
        result += f'{location} - {weather}' + '\n'

    return result


print(
    forecast(
        ("Sofia", "Sunny"),
        ("London", "Cloudy"),
        ("New York", "Sunny")
    )
)

print(
    forecast(
        ("Beijing", "Sunny"),
        ("Hong Kong", "Rainy"),
        ("Tokyo", "Sunny"),
        ("Sofia", "Cloudy"),
        ("Peru", "Sunny"),
        ("Florence", "Cloudy"),
        ("Bourgas", "Sunny")
    )
)

print(
    forecast
        (
        ("Tokyo", "Rainy"),
        ("Sofia", "Rainy")
    )
)
