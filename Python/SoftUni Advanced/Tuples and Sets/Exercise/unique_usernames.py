n_usernames = int(input())
collection = set()
for _ in range(n_usernames):
    username = input()
    collection.add(username)
print("\n".join(collection))
