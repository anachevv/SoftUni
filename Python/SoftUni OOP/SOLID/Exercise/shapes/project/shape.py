from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, *args):
        self.values = args

    @abstractmethod
    def calculate_area(self):
        pass
