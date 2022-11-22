from project.shape import Shape


class Triangle(Shape):
    def __init__(self, *args):
        super().__init__(args)
        self.side = args[0]
        self.height = args[1]

    def calculate_area(self):
        return (self.side * self.height) / 2
