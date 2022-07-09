name_and_phone = input()
contacts = {}

while '-' in name_and_phone:
    name, phone = name_and_phone.split('-')
    if name not in contacts:
        contacts[name] = []
    contacts[name].append(phone)

    name_and_phone = input()

for _ in range(int(name_and_phone)):
    contact = input()
    if contact not in contacts:
        print(f"Contact {contact} does not exist.")
    else:
        print(f"{contact} -> {''.join(contacts[contact])}")
