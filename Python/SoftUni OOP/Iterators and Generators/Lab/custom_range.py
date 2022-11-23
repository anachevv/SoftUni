class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration

        result = self.counter
        self.counter += 1

        return result
