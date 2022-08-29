kids_names = input().split()
n_toss = int(input())
count = 1
removed = []
while len(kids_names) != 1:
    if n_toss == 1:
        for index in range(len(kids_names)):
            index = 0
            if index + 1 == len(kids_names):
                break
            print("Removed {}".format(kids_names[index]))
            kids_names.remove(kids_names[index])
    else:
        new_list = []
        for index in range(len(kids_names)):
            if n_toss > 1 and count % n_toss != 0:
                new_list.append(kids_names[index])
            else:
                print("Removed {}".format(kids_names[index]))
            count += 1

        kids_names = new_list
print("Last is {}".format(kids_names[0]))
