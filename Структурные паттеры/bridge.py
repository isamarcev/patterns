from abc import ABC, abstractmethod



class RackFactory:

    def __init__(self, implementation):
        self._implementation = implementation

    def create(self):
        y = self._implementation.special_name()
        return 'Created' + y


class RackFactoryExtended(RackFactory):

    def get_price_for_seller(self):
        price = self._implementation.give_price()
        return f'{float(price) * 1.2} $'


class WorkShop(ABC):
    @abstractmethod
    def special_name(self):
        pass

class WorkShopWood(WorkShop):
    def special_name(self):
        return ' Wood Racks'

    def give_price(self):
        return 1000


class WorkShopMetal(WorkShop):
    def special_name(self):
        return ' Metal Racks'

    def give_price(self):
        return 35000

class WorkShopGold(WorkShop):
    def special_name(self):
        return ' Golden Racks'

    def give_price(self):
        return 100000000

def client_code(abstraction: RackFactory):

    print('Done:', abstraction.create())
    print('Price:', abstraction.get_price_for_seller())
    print('<', '---' * 10, '>')

if __name__ == "__main__":

    implementation = WorkShopWood()
    abstraction = RackFactoryExtended(implementation)
    client_code(abstraction)

    implementation = WorkShopMetal()
    abstraction = RackFactoryExtended(implementation)
    client_code(abstraction)

    implementation = WorkShopGold()
    abstraction = RackFactoryExtended(implementation)
    client_code(abstraction)