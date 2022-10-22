command = input()
usernames_and_submissions = {}
banned_users = []

languages_and_submissions = {}

while command != 'exam finished':
    command = command.split('-')
    if 'banned' in command:
        banned_username = command[0]
        banned_users.append(banned_username)
    else:
        username, language, points = command[0], command[1], int(command[2])
        if username not in usernames_and_submissions:
            usernames_and_submissions[username] = []
        if language in usernames_and_submissions[username]:
            usernames_and_submissions[username] += [points]
            languages_and_submissions[language] += 1
        else:
            usernames_and_submissions[username] += [language, points]
            if language not in languages_and_submissions:
                languages_and_submissions[language] = 0
            languages_and_submissions[language] += 1

    command = input()

print('Results:')
for user, submission in usernames_and_submissions.items():
    all_points = [element for element in submission if element != submission[0] and isinstance(element, int)]
    max_points = max(all_points)
    if user not in banned_users:
        print(f"{user} | {max_points}")

print('Submissions:')
for language, submissions in languages_and_submissions.items():
    print(f"{language} - {submissions}")
