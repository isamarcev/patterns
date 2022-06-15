class RackFactory():
    def get_price(self):
        pass

class ShelvesRackFactory(RackFactory):
    def __init__(self, length, height, levels, costs_of_materials):
        self.length = length
        self.levels = levels
        self.height = height
        self.costs_of_materials = costs_of_materials

    def get_price(self):
        param = {
            'length': self.length,
            'height': self.height,
            'levels': self.levels,
            'costs': self.length * self.height * self.levels * self.costs_of_materials / 10000
        }
        return (param)

class SalesCompany(RackFactory):

    def __init__(self, factory: RackFactory):
        self._factory = factory

    @property
    def component(self):
        return self._factory

    def get_price(self):
        return self._factory.get_price()

class BestSeller(SalesCompany):

    def get_price(self):
        price = self.component.get_price()
        price['costs'] = float(price['costs']) * 1.2
        return price

class SecontSellerCO(SalesCompany):

    def get_price(self):
        price = self.component.get_price()
        price['costs'] = float(price['costs']) * 1.4
        return price


def client_code(factory: RackFactory):

    print(f'Price for this CO {factory.get_price()}')


if __name__ == "__main__":

    typefactory =ShelvesRackFactory(200, 300, 5, 2 ** 8)
    print('Original:')
    client_code(typefactory)

    print('BestSeller:')

    bestseller =BestSeller(typefactory)
    client_code(bestseller)
    print('Second Seller:')

    secondseller = SecontSellerCO(typefactory)
    client_code(secondseller)


