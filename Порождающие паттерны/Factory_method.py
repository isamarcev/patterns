from abc import ABC, abstractmethod

class WoodAndMetalFactory(ABC):
    def __init__(self, weight, levels, height, costs_of_material):
        self.weight = weight
        self.levels = levels
        self.height = height
        self.costs_of_material = costs_of_material
    @abstractmethod
    def create(self):
        pass


class WorkShopMetal(WoodAndMetalFactory):
    def create(self):
        return MetalRacks(self.weight, self.levels, self.height, self.costs_of_material)


class WorkShopWood(WoodAndMetalFactory):
    def create(self):
        return WoodenRacks(self.weight, self.levels, self.height, self.costs_of_material)


class WorkShopGolden(WoodAndMetalFactory):
    def create(self):
        return GoldenRacks(self.weight, self.levels, self.height, self.costs_of_material)


class Racks(ABC):
    def __init__(self, weight, levels, height, costs_of_material):
        self.weight = weight
        self.levels = levels
        self.height = height
        self.costs_of_material = costs_of_material

    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def get_price(self):
        pass


class MetalRacks(Racks):
    def process(self):
        print("Спроектирован металлический стеллаж")

    def get_price(self):
        price = (self.height / 10000) * (self.levels * self.weight / 10000) * self.costs_of_material
        print(f'Стоимость металлического стеллажа составит: {price}')


class WoodenRacks(Racks):
    def process(self):
        print("Создан деревянный стеллаж")

    def get_price(self):
        price = (self.height / 10000) * (self.levels * self.weight / 10000) * self.costs_of_material
        print(f'Стоимость стеллажа из дерева составит: {price}')


class GoldenRacks(Racks):
    def process(self):
        print("Создан золотой стеллаж")

    def get_price(self):
        price = (self.height / 10000) * (self.levels * self.weight / 10000) * self.costs_of_material
        print(f'Стоимость золотого стеллажа составит: {price}')

if __name__=="__main__":
    request = WorkShopMetal(500, 5, 2000, 35000)
    metal_rack = request.create()
    metal_rack.process()
    metal_rack.get_price()
    print('-' * 60)

    request = WorkShopMetal(100, 2, 1000, 35000)
    metal_rack = request.create()
    metal_rack.process()
    metal_rack.get_price()
    print('-' * 60)

    working = WorkShopWood(500, 5, 2000, 10000)
    wood_rack = working.create()
    wood_rack.process()
    wood_rack.get_price()
    print('-' * 60)

    working = WorkShopGolden(500, 5, 2000, 1500000)
    gold_racks = working.create()
    gold_racks.process()
    gold_racks.get_price()

