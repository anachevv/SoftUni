class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.result = ""

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.result) == self.number:
            raise StopIteration
        if self.counter == len(self.sequence):
            self.counter = 0

        new_seq = self.sequence[self.counter]
        self.result += new_seq
        self.counter += 1
        return new_seq


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
