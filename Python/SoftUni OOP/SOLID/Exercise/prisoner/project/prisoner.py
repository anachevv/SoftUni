from project.free_person import Person


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(Prisoner.PRISON_LOCATION)
        self.is_free = False
