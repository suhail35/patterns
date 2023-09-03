from abc import ABCMeta, abstractmethod


class Reader(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, url: str):
        pass


class ResourceReader:
    def __init__(self, reader: Reader):
        self.__reader = reader

    def set_strategy(self, reader: Reader):
        self.__reader = reader

    def read(self, url: str):
        self.__reader.parse(url)


class NewsSiteReader(Reader):
    def parse(self, url: str):
        print('Parse from news site: ', url)


class SocialNetworkReader(Reader):
    def parse(self, url: str):
        print('Parse from social network: ', url)


class TelegramCannelReader(Reader):
    def parse(self, url: str):
        print('Parse from tg channel: ', url)


if __name__ == '__main__':
    resource_reader = ResourceReader(NewsSiteReader())

    url = 'https://news.com'
    resource_reader.read(url)

    url = 'https://facebook.com'
    resource_reader.set_strategy(SocialNetworkReader())
    resource_reader.read(url)

    url = '@news_channel_telegram'
    resource_reader.set_strategy(TelegramCannelReader())
    resource_reader.read(url)
