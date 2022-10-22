def age_assignment(*args, **kwargs):
    result = ""
    info = {}
    for name in args:
        info[name] = 0
    
    for key, value in kwargs.items():
        for name in info:
            if key == name[0]:
                info[name] = value
    info = sorted(info.items(), key=lambda x: (x[0]))
    
    for person in info:
        name, age = person[0], person[1]
        result += f"{name} is {age} years old." + '\n'

    return result



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
