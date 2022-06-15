class Electricity:
    def __init__(self, power):
        self.power = power


class Charger:
    def __init__(self, needed):
        self.needed = needed

    def charging(self, power):
        if self.needed + 10 < power:
            print('you should buy new Charger')
        elif self.needed - 40 < power < self.needed + 9:
            print('Charging ON')
        else:
            print('Change coefficient transform')

class Transformator(Electricity):
    coefficient = 0.2
    def transform(self):
        v = self.power * self.coefficient
        return v


if __name__ == "__main__":
    power = Transformator(1000).transform()
    charg = Charger(220)
    charg.charging(power)





