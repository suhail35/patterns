"""
Декоратор (Decorator).
Данный шаблон был сформирован для динамического подключения дополнительного поведения к объекту.
С его помощью практика создания подклассов получает гибкую альтернативу.
Это позволяет сделать функционал более широким.
"""

from abc import ABCMeta, abstractmethod


class IProcessor(metaclass=ABCMeta):

    @abstractmethod
    def process(self):
        pass


class Transmitter(IProcessor):
    def __init__(self, data: str):
        self.__data = data

    def process(self):
        print(f'Data {self.__data} send by channel')


class Shell(IProcessor):
    def __init__(self, pr: IProcessor):
        self._processor = pr

    @abstractmethod
    def process(self):
        self._processor.process()


class HammingCoder(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('Tolerant coder added', end='')
        self._processor.process()


class Encryptor(Shell):
    def __init__(self, pr: IProcessor):
        super().__init__(pr)

    def process(self):
        print('Encryption added', end='')
        self._processor.process()


if __name__ == '__main__':
    trans: IProcessor = Transmitter('12345')
    trans.process()

    ham: Shell = HammingCoder(trans)
    ham.process()

    encrypt: Shell = Encryptor(trans)
    encrypt.process()
