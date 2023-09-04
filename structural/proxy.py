"""
Заместитель (Proxy).
Он предоставляет объект, контролирующий доступ к другому объекту, перехватывая при этом все вызовы.
Иными словами, он выступает в качестве контейнера Фасад (Facade).
Он помогает скрыть сложность системы.
Принцип работы довольно прост: все возможные внешние вызовы сводятся к одному и тому же объекту,
который передаёт эти вызовы соответствующим объектам системы.
"""
from abc import ABCMeta, abstractmethod
from typing import Dict


class ISite(metaclass=ABCMeta):
    @abstractmethod
    def get_page(self, num: int):
        pass


class Site(ISite):
    def get_page(self, num: int) -> str:
        return f'This is the page {num}'


class SiteProxy(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__cache.get(num):
            page = self.__cache[num]
            page = 'from cache ' + page
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page
        return page


if __name__ == '__main__':
    my_site: ISite = SiteProxy(Site())
    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))
    print(my_site.get_page(2))

