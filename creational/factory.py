"""
Factory (Фабрика).
Это не считается паттерном в строгом смысле слова.
Правильнее будет обозначить Factory как подход,
в рамках которого логика создания объектов выносится в отдельный класс.
"""
class IProduct:
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print("Car released")


class Truck(IProduct):
    def release(self):
        print('Truck released')


class IWorkShop:
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self):
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self):
        return Truck()


if __name__ == '__main__':
    creator = CarWorkShop()
    car = creator.create()

    creator = TruckWorkShop()
    truck = creator.create()

    car.release()
    truck.release()

