from project.icontent import IContent


class MyContent(IContent):
    def __init__(self, text):
        super().__init__(text)

    def display(self):
        return ''.join(['<MyML>', self.text, '</MyML>'])
