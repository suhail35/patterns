from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, emp: 'Employee', msg: str):
        pass


class Employee(metaclass=ABCMeta):
    def __init__(self, mediator: IMediator):
        self._mediator = mediator

    def set_mediator(self, med: IMediator):
        self._mediator = med


class Designer(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__is_working = False

    def execute_work(self):
        print('Designer working')
        self._mediator.notify(self, 'Designer projecting')

    def set_work(self, state: bool):
        self.__is_working = state
        if state:
            print('Designer free')
        else:
            print('Designer busy')


class Director(Employee):
    def __init__(self, med: IMediator = None):
        super().__init__(med)
        self.__text: str = None

    def give_command(self, txt: str):
        self.__text = txt
        if txt == '':
            print('Boss know that designer is busy')
        else:
            print(f'Boss send command {txt}')
        self._mediator.notify(self, txt)


class Controller(IMediator):
    def __init__(self, designer: Designer, director: Director):
        self.__designer = designer
        self.__director = director
        designer.set_mediator(self)
        director.set_mediator(self)

    def notify(self, emp: 'Employee', msg: str):
        if isinstance(emp, Director):
            if msg == '':
                self.__designer.set_work(False)
            else:
                self.__designer.set_work(True)

        if isinstance(emp, Designer):
            if msg == 'Designer projecting':
                self.__director.give_command('')


if __name__ == '__main__':
    designer_ = Designer()
    director_ = Director()

    mediator_ = Controller(designer_, director_)
    director_.give_command('Project')
    designer_.execute_work()
