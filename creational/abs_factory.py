"""
Абстрактная фабрика (Abstract factory).
Это порождающий паттерн проектирования, который предоставляет интерфейс для создания семейств взаимосвязанных
или взаимозависимых объектов, без непосредственной спецификации их конкретных классов.
Реализация такого шаблона обеспечивается за счёт создания абстрактного класса Factory.
Этот класс выступает в качестве интерфейса для создания компонентов системы
(скажем, применительно к оконному интерфейсу он может формировать окна и кнопки).
После всего этого пишутся классы, которые реализуют данный интерфейс.
"""
from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_ingine(self):
        pass


class JapaneseEngine(IEngine):
    def release_ingine(self):
        print('j_ingine create')


class RussianEngine(IEngine):
    def release_ingine(self):
        print('r_ingine create')


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, ingine: IEngine):
        pass


class JapaneseCar(ICar):
    def release_car(self, ingine: IEngine):
        print('J_car create', end=' ')
        ingine.release_ingine()


class RussianCar(ICar):
    def release_car(self, ingine: IEngine):
        print('R_car create', end=' ')
        ingine.release_ingine()


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_ingine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):
    def create_ingine(self) -> IEngine:
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()


class RussianFactory(IFactory):
    def create_ingine(self) -> IEngine:
        return RussianEngine()

    def create_car(self) -> ICar:
        return RussianCar()


if __name__ == '__main__':
    j_factory = JapaneseFactory()
    j_engine = j_factory.create_ingine()
    j_car = j_factory.create_car()

    j_car.release_car(j_engine)

    r_factory = RussianFactory()
    r_engine = r_factory.create_ingine()
    r_car = r_factory.create_car()

    r_car.release_car(r_engine)
