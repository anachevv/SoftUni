import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# Custom Errors
class OneAtSymbolOnlyError(Exception):
    pass


class InvalidNameError(Exception):
    pass


valid_domains = ['.com', '.bg', '.org', '.net']

email = input()
while email != 'End':
    all_regex = r"^([a-z0-9]+[a-z0-9_\.-]*)@([a-z]+)(\.[a-z]+)$"
    all_pattern = re.findall(all_regex, email)
    try:
        if email.count('@') != 1:
            if email.count('@') == 0:
                raise MustContainAtSymbolError("Email must contain @")
            raise OneAtSymbolOnlyError("Email must contain one At symbol only!")

        if all_pattern:
            if len(email.split('@')[0]) <= 4:
                raise NameTooShortError("Name must be more than 4 characters")
            if all_pattern[0][-1] not in valid_domains:
                raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domains)}")
        else:
            raise InvalidNameError("Invalid email name")

        print("Email is valid")

    except IndexError:
        print("Invalid email")

    email = input()
