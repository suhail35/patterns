"""
Наблюдатель (Observer).
Его также называют «подчинённые» (Dependents).
Формирует особый механизм у класса, который даёт возможность экземпляру объекта этого класса
получать уведомления от остальных объектов.
В оповещения содержится информация об изменении их состояния. Таким образом, происходит наблюдение за объектом.
"""
from abc import ABCMeta, abstractmethod
from typing import List


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, p: int):
        pass


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def add_observer(self, o: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, o: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class Product(IObservable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers: List[IObserver] = []

    def change_price(self, price: int):
        self.__price = price
        self.notify()

    def add_observer(self, o: IObserver):
        self.__observers.append(o)

    def remove_observer(self, o: IObserver):
        self.__observers.remove(o)

    def notify(self):
        for o in self.__observers:
            o.update(self.__price)


class Wholesale(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 300:
            print(f'Wholesale bought goods for price {p}')
            self.__product.remove_observer(self)


class Buyer(IObserver):
    def __init__(self, obj: IObservable):
        self.__product = obj
        obj.add_observer(self)

    def update(self, p: int):
        if p < 350:
            print(f'Buyer bought goods for price {p}')
            self.__product.remove_observer(self)


if __name__ == '__main__':
    product = Product(400)
    wholesale = Wholesale(product)
    buyer = Buyer(product)

    product.change_price(320)
    product.change_price(250)
