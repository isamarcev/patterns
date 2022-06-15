class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, *kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DirectorOfSpaceX(metaclass=SingletonMeta):
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_all(self):
        return self.name, self.age, self.position

class DirectorOfFacebook(metaclass=SingletonMeta):
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_all(self):
        return self.name, self.age, self.position

if __name__ == '__main__':
    x = DirectorOfSpaceX('Elon Musk', 45, 'Owner')
    y = DirectorOfFacebook('Mark Tsukerberg', 34, 'Director')
    x1 = DirectorOfSpaceX('Mark Tsukerberg', 34, 'Director')
    y1 = DirectorOfFacebook('Elon Musk', 45, 'Owner')
    print(x.get_all())
    print(y.get_all())
    print(x1.get_all())
    print(y1.get_all())