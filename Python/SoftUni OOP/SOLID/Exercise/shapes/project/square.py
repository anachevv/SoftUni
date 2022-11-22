from project.shape import Shape


class Square(Shape):
    def __init__(self, *args):
        super().__init__(args)
        self.side = args[0]

    def calculate_area(self):
        return self.side ** 2
