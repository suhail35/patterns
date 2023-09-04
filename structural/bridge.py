"""
Мост (Bridge).
Применяется в проектировании ПО.
Он разделяет абстракцию и реализацию таким образом, чтобы они могли меняться независимо.
Данный паттерн работает с помощью инкапсуляции, агрегирования и может применять наследование
в целях распределения межклассовой ответственности.
"""
from abc import ABCMeta, abstractmethod


class IDataReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        pass


class DatabaseReader(IDataReader):
    def read(self):
        print('read from database')


class FileReader(IDataReader):
    def read(self):
        print('read from file')


class Sender(metaclass=ABCMeta):
    def __init__(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    def set_data_reader(self, data_reader: IDataReader):
        self.reader: IDataReader = data_reader

    @abstractmethod
    def send(self):
        pass


class EmailSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('by Email send')


class TelegramBotSender(Sender):
    def __init__(self, data_reader: IDataReader):
        super().__init__(data_reader)

    def send(self):
        self.reader.read()
        print('Send by telegram bot')


if __name__ == '__main__':
    sender: Sender = EmailSender(DatabaseReader())
    sender.send()

    sender.set_data_reader(FileReader())
    sender.send()

    sender = TelegramBotSender(DatabaseReader())
    sender.send()
