from project.shape import Shape


class Rectangle(Shape):
    def __init__(self, *args):
        super().__init__(args)
        self.width = args[0]
        self.length = args[1]

    def calculate_area(self):
        return self.width * self.length
