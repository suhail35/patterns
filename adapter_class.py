from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):

    @abstractmethod
    def get_weight(self) -> float:
        pass

    @abstractmethod
    def adjust(self):
        pass


class RussianScale(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight

    def adjust(self):
        print('Adjust ru scale')


class BritishScale:
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight

    def adjust(self):
        print('Adjust british scale')


class AdapterBritishScale(BritishScale, IScale):
    def __init__(self, cw: float):
        super().__init__(cw)

    def get_weight(self) -> float:
        return super().get_weight() * .453

    def adjust(self):
        super().adjust()
        print('Adapter adjust scale')


if __name__ == '__main__':
    r_c: IScale = RussianScale(55)
    b_c: IScale = AdapterBritishScale(55)

    print(r_c.get_weight())
    print(b_c.get_weight())

    r_c.adjust()
    b_c.adjust()
