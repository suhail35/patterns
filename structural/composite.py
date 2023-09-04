"""
Компоновщик (Composite pattern).
Такой шаблон способен объединять объекты в древовидную структуру.
Это полезно для представления иерархии от частного к целому.
Тем самым Composite pattern даёт клиентам возможность обращаться к отдельным объектам и
к группам объектов одинаковым образом.
"""
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner_name: str = None

    def set_owner(self, o: str):
        self._owner_name: str = o

    @abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def remove(self, sub_item: 'Item'):
        pass

    @abstractmethod
    def display(self):
        pass


class ClickableItem(Item):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception("add sub item not allowed")

    def remove(self, sub_item: 'Item'):
        raise Exception("remove sub item not allowed")

    def display(self):
        print(self._owner_name + self._item_name)


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self.__children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self._item_name)
        self.__children.append(sub_item)

    def remove(self, sub_item: Item):
        self.__children.remove(sub_item)

    def display(self):
        for item in self.__children:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()


if __name__ == '__main__':
    file: Item = DropDownItem('File->')

    create: Item = DropDownItem('Create->')
    open_: Item = DropDownItem('Open->')
    exit_: Item = ClickableItem('Exit')

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project: Item = ClickableItem('Project...')
    repository: Item = ClickableItem('Repository...')

    create.add(project)
    create.add(repository)

    solution: Item = ClickableItem('Solution...')
    folder: Item = ClickableItem('Folder...')

    open_.add(solution)
    open_.add(folder)

    file.display()

    file.remove(create)

    file.display()
