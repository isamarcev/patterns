from abc import ABC, abstractmethod


class Component(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, component):
        self._parent = component

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def name(self):
        pass

class Rack(Component):
    __name = "Rack"
    __salesworker = 200
    def __init__(self, height, thickness, width, costs_of_material, man_hours, density = 7.200):
        self.height = height
        self.thickness = thickness
        self.width = width
        self.density = density
        self.costs_of_material = costs_of_material
        self.man_hours = man_hours

    def get_price(self):
        price = 0.2 * ((self.height * self.thickness * self.width) * self.density * self.costs_of_material) + self.man_hours * self.__salesworker
        return int(price)

    def name(self):
        return self.__name


class Shelves(Component):
    __name = "Shelve"
    __salesworker = 200

    def __init__(self, height, thickness, width, costs_of_material, man_hours, density = 7.200):
        self.height = height
        self.thickness = thickness
        self.width = width
        self.density = density
        self.costs_of_material = costs_of_material
        self.man_hours = man_hours

    def get_price(self):
        price = 0.2 * ((self.height * self.thickness * self.width) * self.density * self.costs_of_material) + self.man_hours * self.__salesworker
        return int( price)

    def name(self):
        return self.__name

class Binding(Component):
    __name = "Binding"

    def __init__(self, amount, costs_of_material):
        self.amount = amount
        self.costs_of_material = costs_of_material

    def get_price(self):
        price = (self.costs_of_material * self.amount)
        return int( price)

    def name(self):
        return self.__name


class FullRack(Component):

    def __init__(self):
        self._children = []


    def is_composite(self):
        return True

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component):
        self._children.remove(component)
        component.parent = None

    def get_price(self):

        all_price = 0
        for i in self._children:
            all_price += i.get_price()

        return f'Price all elements: {all_price}$'

    def name(self):
        all_names = []
        for i in self._children:
            all_names.append(i.name())
        return f"Rack consist of: {', '.join(all_names)}."

def client_code(component: Component):

    print(component.name(), component.get_price(), end='\n')

def client_code2(component1: Component, component2: Component):

    if component1.is_composite():
        component1.add(component2)

    print('Order consist of:', component1.name())

    print(component1.get_price())

if __name__ == '__main__':

    rack = Rack(2, 0.08, 0.6, 35000, 2)
    shelve = Shelves(1.2, 0.08, 1, 20000, 1.2, 6)
    binding = Binding(4, 299)
    composite = FullRack()

    client_code(rack), client_code(shelve), client_code(binding)

    composite.add(rack)
    composite.add(binding)
    composite.add(shelve)
    client_code(composite)

    print('____' * 20)

    tree = FullRack()
    tree.add(rack)
    tree.add(shelve)
    tree.add(shelve)

    client_code2(tree, rack)



