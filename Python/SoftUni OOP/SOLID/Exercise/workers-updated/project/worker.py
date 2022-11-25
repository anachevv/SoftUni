from abc import abstractmethod
from time import sleep


class Workable:
    @abstractmethod
    def work(self):
        pass


class Eatable:
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        sleep(5)
