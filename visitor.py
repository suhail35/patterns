from abc import ABCMeta, abstractmethod
from typing import List


class IVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, place: 'IPlace'):
        pass


class IPlace(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


class Zoo(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Cinema(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class Circus(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class HolidayMarker(IVisitor):
    def __init__(self):
        self.value = ''

    def visit(self, place: 'IPlace'):
        if isinstance(place, Zoo):
            self.value = 'Elephant in zoo'
        elif isinstance(place, Cinema):
            self.value = 'Lord of rings'
        elif isinstance(place, Circus):
            self.value = 'Clone in circus'


if __name__ == '__main__':
    places: List[IPlace] = [Zoo(), Cinema(), Circus()]

    for place_ in places:
        visitor_ = HolidayMarker()
        place_.accept(visitor_)
        print(visitor_.value)
