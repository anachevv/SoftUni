import sys


class CustomList(Exception):
    def __init__(self):
        self.lst = []

    def append(self, value):
        self.lst.append(value)
        return self.lst

    def remove(self, value):
        try:
            self.lst.remove(value)
            return self.lst
        except ValueError:
            raise Exception(f"{value} not found!")

    def get(self, index):
        try:
            return self.lst[index]
        except IndexError:
            raise Exception(f"No such index: {index}")

    def extend(self, iterable):
        self.lst.extend(iterable)
        return self.lst

    def insert(self, index, value):
        self.lst.insert(index, value)
        return self.lst

    def pop(self):
        try:
            return self.lst.pop()
        except IndexError:
            raise Exception("List is empty!")

    def clear(self):
        return self.lst.clear()

    def index(self, value):
        try:
            return self.lst.index(value)
        except ValueError:
            raise Exception(f"{value} not in list!")

    def count(self, value):
        return self.lst.count(value)

    def reverse(self):
        self.lst.reverse()
        return self.lst

    def copy(self):
        return self.lst.copy()

    def size(self):
        return len(self.lst)

    def add_first(self, value):
        self.lst.insert(0, value)
        return self.lst

    def dictionize(self):
        dct = {}
        for idx in range(len(self.lst)):
            if idx % 2 == 0 and idx < len(self.lst) - 1:
                dct[self.lst[idx]] = self.lst[idx + 1]
            elif idx % 2 == 0 and idx == len(self.lst) - 1:
                dct[self.lst[idx]] = ' '

        return dct

    def move(self, amount):
        if amount >= len(self.lst):
            raise Exception("List cannot be rearranged!")
        self.lst.extend(self.lst[:amount])
        self.lst = self.lst[amount::]
        return self.lst

    def sum(self):
        if not self.lst:
            raise Exception("List is empty!")
        sum = 0
        for el in self.lst:
            if type(el) in (int, float):
                sum += el
            else:
                sum += len(el)

        return sum

    def overbound(self):
        if not self.lst:
            raise Exception("List is empty!")
        max_value = -sys.maxsize
        for el in self.lst:
            if type(el) in (int, float):
                if el > max_value:
                    max_value = el
            else:
                if len(el) > max_value:
                    max_value = len(el)

        return max_value

    def underbound(self):
        if not self.lst:
            raise Exception("List is empty!")
        min_value = sys.maxsize
        for el in self.lst:
            if type(el) in (int, float):
                if el < min_value:
                    min_value = el
            else:
                if len(el) < min_value:
                    min_value = len(el)

        return min_value


l = CustomList()
