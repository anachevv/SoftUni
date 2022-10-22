def password_validator(passphrase):

    password_is_valid = True

    if len(passphrase) < 6 or len(passphrase) > 10:
        print("Password must be between 6 and 10 characters")
        password_is_valid = False

    if not passphrase.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False

    if (sum(c.isdigit() for c in passphrase)) < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False

    return password_is_valid


password = input()

is_valid = password_validator(password)

if is_valid:
    print('Password is valid')
