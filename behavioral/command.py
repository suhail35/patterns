"""
Команда (Command).
Он представляет действие и применяется в рамках объектно-ориентированного программирования.
Объект команды содержит в себе как само действие, так и его параметры.
"""
from abc import ABCMeta, abstractmethod
from typing import List, Deque


class ICommand(metaclass=ABCMeta):
    @abstractmethod
    def positive(self):
        pass

    @abstractmethod
    def negative(self):
        pass


class Conveyor:
    def on(self):
        print('conveyor on')

    def off(self):
        print('conveyor off')

    def speed_increase(self):
        print('speed up')

    def speed_decrease(self):
        print('speed down')


class ConveyorWorkCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.on()

    def negative(self):
        self.conveyor.off()


class ConveyorAdjustCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decrease()


class Multipult:
    def __init__(self):
        self.__commands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__commands[button] = command

    def press_on(self, button: int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        if len(self.__history) != 0:
            self.__history.pop().negative()


if __name__ == '__main__':
    conveyor = Conveyor()

    multipult = Multipult()

    multipult.set_command(0, ConveyorWorkCommand(conveyor))
    multipult.set_command(1, ConveyorAdjustCommand(conveyor))

    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()
