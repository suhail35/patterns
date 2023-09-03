class ProviderCommunication:
    def receive(self):
        print('Receive products')

    def payment(self):
        print('Paying to supplements')


class Site:
    def placement(self):
        print('Place to site')

    def delete(self):
        print('Remove from site')


class Database:
    def insert(self):
        print('Insert to DB')

    def delete(self):
        print('Delete from DB')


class MarketPlace:
    def __init__(self):
        self._provider_communication = ProviderCommunication()
        self._site = Site()
        self._database = Database()

    def product_receive(self):
        self._provider_communication.receive()
        self._site.placement()
        self._database.insert()

    def product_release(self):
        self._provider_communication.payment()
        self._site.delete()
        self._database.delete()


if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receive()
    market_place.product_release()

