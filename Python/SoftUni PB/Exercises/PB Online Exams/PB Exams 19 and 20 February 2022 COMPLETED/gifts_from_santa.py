n_number = int(input())
m_number = int(input())
s_number = int(input())

for gift in range(m_number, n_number, - 1):
    if gift % 6 == 0:
        if gift != s_number:
            print(f"{gift}", end=" ")
        elif gift == s_number:
            break
