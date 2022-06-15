class Electricity:
    def __init__(self, power):
        self.power = power


class Charger:
    def __init__(self, power):
        self.power = power

    def charging(self):
        if 180 <=  self.power <= 230:
            print('Charign ON')
        elif self.power > 230:
            print('you should buy new Charger')
        else:
            print('Change coefficient of transform')

class Transformator(Electricity):
    coefficient = 0.2
    def transform(self):
        v = self.power * self.coefficient
        return v


if __name__ == "__main__":
    power = Transformator(1000).transform()
    charg = Charger(power)
    charg.charging()





