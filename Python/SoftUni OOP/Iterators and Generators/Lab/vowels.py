class vowels:
    VOWELS = 'aeiouy'

    def __init__(self, text: str):
        self.vowels_in_text = [letter for letter in text if letter.lower() in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)
