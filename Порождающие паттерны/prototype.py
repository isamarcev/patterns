import copy
from abc import ABC, abstractmethod

from Abstract_factory import ShopRacksFactory
from Factory_method import WorkShopMetal


class Prototype(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def clone(self):
        pass

class ConcretePrototype(Prototype):
    def clone(self):
        return copy.deepcopy(self.data)


if __name__ == "__main__":
    info = [1, 2, 3, [2, 4, 5]]
    x = ConcretePrototype(info).clone()
    print('x is info?', x is info)
    print('x= ', x)
    info.append('Agent')
    print('info =', info, '!    x = ', x)


    #
    # data = ConcretePrototype(info)
    # clone_maker = CloneMaker(data)
    # data_clone_1 = clone_maker.make_clone()
    # data_clone_2 = clone_maker.make_clone()
    # print(id(data))
    # print(data, data_clone_1, data_clone_2)
    # print(data_clone_1 == data_clone_2)



# class SomeObject:
#
#     def __init__(self, some_object):
#         self.some_object = some_object
#
#     def __copy__(self):
#         new_object = copy.copy(self.some_object)
#         new = self.__class__(new_object        )
#         new.__dict__.update(self.__dict__)
#         return new
#
#     def clone(self):
#         new_object = copy.deepcopy(self.some_object)
#         return new_object
#
#     def __deepcopy__(self, memo = None):
#         if memo is None:
#             memo = {}
#         new_object = copy.deepcopy(self.some_object, memo)
#         new = self.__class__(new_object)
#         new.__dict__= copy.deepcopy(self.__dict__, memo)
#         return new

# if __name__ == "__main__":
#
#     data = SomeObject('Ilon')
#     clone = ConcretePrototype(data)
#
#     print(clone)

    # list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    # component = SomeObject(list_of_objects)
    #
    # jjjj = component.__deepcopy__()
    # print(jjjj)
    # print(list_of_objects == jjjj)
    #
    # shallow_copied_component = copy.copy(component)
    #
    # shallow_copied_component.some_object.append("another object")
    # print(shallow_copied_component.some_object, list_of_objects)
    #
    # component.some_object[1].add(4)
    # print(shallow_copied_component.some_object, list_of_objects)
    #
    # deep_copied_component = copy.deepcopy(component)
    #
    # deep_copied_component.some_object.append("one more object")
    # print(deep_copied_component.some_object, list_of_objects)
    #
    # component.some_object[1].add(10)
    # print(deep_copied_component.some_object, list_of_objects)
    #
