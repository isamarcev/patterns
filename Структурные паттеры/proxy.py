import datetime
import json
import time
from abc import ABC, abstractmethod

class CoffeePoint(ABC):
    menu = {
        'americano': 10,
        'espresso':8
    }
    @abstractmethod
    def make_coffee(self):
        pass

    def get_price(self):
        pass

class CoffeeOrder(CoffeePoint):
    def __init__(self, name):
        self.name = name

    def make_coffee(self):
        if self.name in self.menu.keys():
            return (f'Coffee {self.name} ordered')
        else:
            print('Pass')

    def get_price(self):
        bill = f'{self.menu[self.name]} $'
        return bill

class ProxyCoffee(CoffeePoint):

    def __init__(self, order: CoffeeOrder):
        self._order = order

    def make_coffee(self):
        if self.chek_request():
            request = {str(datetime.datetime.now().strftime('%d/%m/%y %H:%M')): (self._order.make_coffee(),self._order.get_price())}
            self.save_request(request)
            return request

    def chek_request(self):
        return True

    def save_request(self, request):
        with open("../data/coffeelogger.json", 'a') as   f:
            json.dump(request, f, ensure_ascii=False)

def client_code(original: CoffeePoint):

    return original.make_coffee()



if __name__ == "__main__":
    americano = CoffeeOrder('americano')
    espresso = CoffeeOrder('espresso')

    y = ProxyCoffee(americano)
    y1 = ProxyCoffee(espresso)
    print(client_code(y))
    print(client_code(y1))




