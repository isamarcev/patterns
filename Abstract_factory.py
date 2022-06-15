from abc import ABC, abstractmethod

class AbstractFactoryRacks(ABC):

    def __init__(self, length, height):
        self.length = length
        self.height = height

    @abstractmethod
    def create_shelf(self):
        pass

    @abstractmethod
    def create_rack(self):
        pass

class ShopRacksFactory(AbstractFactoryRacks):

    def create_rack(self):
        return ShopRack(self.height)

    def create_shelf(self):
        return ShopShelf(self.length)

class StoreRacksFactory(AbstractFactoryRacks):
    def create_rack(self):
        return PalletRack(self.height)

    def create_shelf(self):
        return PalletShelf(self.length)

class ShelvesRacksFactory(AbstractFactoryRacks):
    def create_rack(self):
        return ShelvesRack(self.height)

    def create_shelf(self):
        return ShelvesShelf(self.length)

class AbstractShelves(ABC):
    def __init__(self, length):
        self.length = length

    @abstractmethod
    def return_shelf(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class ShopShelf(AbstractShelves):
    def return_shelf(self):
        return f'Created shelves for shop racks'

    def get_price(self):
        price = self.length / 2
        return f'Price Shop Shelf ={price} $ '

class PalletShelf(AbstractShelves):
    def return_shelf(self):
        return 'Created shelves for pallet racks'

    def get_price(self):
        price = self.length * 2
        return f'Price Pallet Shelf = {price} $ '


class ShelvesShelf(AbstractShelves):
    def return_shelf(self):
        return 'Created shelves for shelves racks'

    def get_price(self):
        price = self.length / 5
        return f'Price Shelves Shelf = {price} $ '


class AbstractRack(ABC):

    def __init__(self, height):
        self.height = height

    @abstractmethod
    def return_rack(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class ShopRack(AbstractRack):

    def return_rack(self):
        return 'Created Rack for shop racks'

    def get_price(self):
        price = self.height * 2
        return f'Price Shop Rack = {price} $ '


class PalletRack(AbstractRack):
    def return_rack(self):
        return 'Created rack for pallet racks'

    def get_price(self):
        price = self.height * 5
        return f'Price Pallet Rack = {price} $ '


class ShelvesRack(AbstractRack):
    def return_rack(self):
        return 'Created rack for shelves racks'

    def get_price(self):
        price = self.height / 5
        return f'Price Shelves Rack = {price} $ '


def client_code(fabrika: AbstractFactoryRacks):

    shelve = fabrika.create_shelf()
    rack = fabrika.create_rack()

    print(f'{shelve.return_shelf()}', '------------>>>', f'{shelve.get_price()}')
    print(f'{rack.return_rack()}','------------>>>', f'{rack.get_price()}')
    print('-' * 80)


if __name__ == '__main__':
    client_code(ShopRacksFactory(2000, 5000))
    client_code(ShelvesRacksFactory(2000, 5000))
    client_code(StoreRacksFactory(2000, 5000))
