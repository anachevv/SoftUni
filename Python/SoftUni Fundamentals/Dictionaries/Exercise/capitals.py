countries = input().split(', ')
capitals = input().split(', ')

dct = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in dct.items():
    print(f"{country} -> {capital}")
