class dictionary_iter:
    def __init__(self, dictionary):
        self.info = [x for x in dictionary.items()]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.info) == 0:
            raise StopIteration

        return self.info.pop(0)
