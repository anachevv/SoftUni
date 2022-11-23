class reverse_iter:
    def __init__(self, numbers):
        self.numbers = list(numbers)

    def __iter__(self):
        return self

    # def __reversed__(self):
    #     pass
    def __next__(self):
        if not self.numbers:
            raise StopIteration

        return self.numbers.pop()
