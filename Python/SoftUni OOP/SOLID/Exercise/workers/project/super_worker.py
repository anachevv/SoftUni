from project.worker import BaseWorker


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")
