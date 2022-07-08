class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


list_of_emails = []
command = input()

while command != 'Stop':
    if command == 'Stop':
        break
    command = command.split(' ')
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    list_of_emails.append(email)

    command = input()

indices = [int(x) for x in input().split(', ')]

for element in indices:
    list_of_emails[element].send()

for email in list_of_emails:
    print(email.get_info())
