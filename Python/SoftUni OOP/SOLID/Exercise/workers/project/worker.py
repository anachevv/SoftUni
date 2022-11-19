from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")
