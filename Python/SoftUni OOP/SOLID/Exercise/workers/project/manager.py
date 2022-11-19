from project.worker import BaseWorker, Worker


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), f'`worker` must be of type {Worker}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
