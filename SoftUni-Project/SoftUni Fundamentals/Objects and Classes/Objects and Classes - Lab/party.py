class Party:

    def __init__(self):
        self.lst = []


party = Party()


command = input()
while command != 'End':
    party.lst.append(command)

    command = input()


print('Going: ' + ', '.join(x for x in party.lst))
print('Total: ' + str(len(party.lst)))
