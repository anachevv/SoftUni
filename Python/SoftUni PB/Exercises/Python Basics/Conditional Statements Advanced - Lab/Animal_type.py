user_input = input()
mammal = {"dog"}
reptile = {"crocodile", "tortoise", "snake"}

if user_input in mammal:
    print("mammal")
elif user_input in reptile:
    print("reptile")
else:
    print("unknown")
