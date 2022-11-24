class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count * self.step:
            raise StopIteration

        result = self.counter
        self.counter += self.step

        return result
