from abc import ABCMeta, abstractmethod


class IWorker(metaclass=ABCMeta):
    @abstractmethod
    def set_net_worker(self, worker: 'IWorker') -> 'IWorker':
        pass

    @abstractmethod
    def execute(self, command: str) -> str:
        pass


class AbsWorker(IWorker):
    def __init__(self):
        self.__next_worker: IWorker = None

    def set_net_worker(self, worker: 'IWorker') -> 'IWorker':
        self.__next_worker = worker
        return worker

    def execute(self, command: str) -> str:
        if self.__next_worker:
            return self.__next_worker.execute(command)
        return ''


class Designer(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'design':
            return f'Designer {command} house'
        else:
            return super().execute(command)


class Carpenter(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'carpet':
            return f'Carpenter {command} a wall'
        else:
            return super().execute(command)


class Painter(AbsWorker):
    def execute(self, command: str) -> str:
        if command == 'paint':
            return f'Painter {command} the house'
        else:
            return super().execute(command)


def give_command(worker: IWorker, command: str):
    string: str = worker.execute(command)
    if string:
        print(string)
    else:
        print('Nobody do this work')


if __name__ == '__main__':
    designer = Designer()
    car = Carpenter()
    paint = Painter()

    designer.set_net_worker(car).set_net_worker(paint)

    give_command(designer, 'design')
    give_command(designer, 'carpet')
    give_command(designer, 'paint')
    give_command(designer, 'build')
