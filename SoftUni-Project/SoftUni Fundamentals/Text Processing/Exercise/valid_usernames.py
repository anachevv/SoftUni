def validation(usernames):
    valid_usernames = []

    for username in usernames:
        if 3 <= len(username) <= 16:
            if username.isalnum():
                valid_usernames.append(username)
            elif '-' in username:
                if username.replace('-', '').isalnum():
                    valid_usernames.append(username)
            elif '_' in username:
                if username.replace('_', '').isalnum():
                    valid_usernames.append(username)

    return "\n".join(valid_usernames)


usernames = input().split(', ')

print(validation(usernames))
