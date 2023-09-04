"""
Приспособленец (Flyweight, «легковесный (элемент)»).
В процессе применения данного паттерна объект представляет себя как уникальный экземпляр
в разных частях программы, однако, на самом деле это не так.
"""
from typing import List, Dict


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print(f'New data view common {self.__shared.company}_{self.__shared.position}'
              f'and unique data {unique.name}_{unique.passport}')

    def get_data(self) -> str:
        return self.__shared.company + self.__shared.position


class FlyweightFactory:

    def get_key(self, shared: Shared):
        return f'{shared.company}_{shared.position}'

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweight(self, shared: Shared):
        key: str = self.get_key(shared)
        if self.__flyweights.get(key) is None:
            print(f'Cannot find by key {key}. Creating new.')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print(f'Getting item by key: {key}')
        return self.__flyweights[key]

    def list_flyweights(self):
        count: int = len(self.__flyweights)
        print(f'Total records: {count}')
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_db(ff: FlyweightFactory,
           company: str, position: str, name: str, passport: str):
    print('============')
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__main__':

    shared_list: List[Shared] = (
        Shared('Microsoft', 'Manager'),
        Shared('Google', 'Android-dev'),
        Shared('Google', 'WEB-dev'),
        Shared('Apple', 'IOS-dev')
    )

    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()

    add_db(factory,
           'Google',
           'WEB-dev',
           'Boris',
           'AM-223311')

    add_db(factory,
           'Apple',
           'Manager',
           'Alex',
           'QA-112233')

