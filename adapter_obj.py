from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):

    @abstractmethod
    def get_weight(self) -> float:
        pass


class RuScale(IScale):

    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class BrScale(IScale):
    def __init__(self, cw: float):
        self.__current_weight = cw

    def get_weight(self) -> float:
        return self.__current_weight


class AdapterForBrScale(IScale):
    def __init__(self, br_scale: BrScale):
        self.__br_scale = br_scale

    def get_weight(self) -> float:
        return self.__br_scale.get_weight() * .453


if __name__ == '__main__':
    kg: float = 55
    lb: float = 55

    ru_scale = RuScale(kg)
    br_scale = AdapterForBrScale(BrScale(lb))

    print(ru_scale.get_weight())
    print(br_scale.get_weight())
