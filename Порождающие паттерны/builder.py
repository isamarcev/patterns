from abc import ABC, abstractmethod
from typing import Any

class Manager(ABC):

    @property
    @abstractmethod
    def project(self):
        pass

    @abstractmethod
    def get_task(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def implement(self):
        pass

    @abstractmethod
    def visual_project(self):
        pass

    @abstractmethod
    def do_document(self):
        pass

    @abstractmethod
    def false_sales(self):
        pass


class ShopManager(Manager):

    def __init__(self):
        self.reset()

    def reset(self):
        self._project = ProjectShopMall()

    @property
    def project(self):
        project_shop = self._project
        self.reset()
        return project_shop

    def get_task(self):
        self._project.add('Получили проект для магазина!')

    def visual_project(self):
        self._project.add('Сделали супер дизайн проект!')

    def sell(self):
        self._project.add('Продали, отправляем чертежи на завод! ')

    def implement(self):
        self._project.add('Все готово к сборке! ')

    def do_document(self):
        self._project.add('Документы подписаны, все довольны! ')

    def false_sales(self):
        self._project.add('Сорвалась продажа.')

class TenderManager(Manager):

    def __init__(self):
        self.reset()

    def reset(self):
        self._project = ProjectTender()

    @property
    def project(self):
        project_shop = self._project
        self.reset()
        return project_shop

    def get_task(self):
        self._project.add('Нашли Тендер')

    def visual_project(self):
        self._project.add('Сделали проект и стоимость')

    def sell(self):
        self._project.add("Money is here")

    def implement(self):
        self._project.add('Товар у клиента')

    def do_document(self):
        self._project.add("Документы подписаны!")

    def false_sales(self):
        self._project.add('Потрачено время впустую!')


class ProjectShopMall():
    def __init__(self):
        self.all_project = []

    def add(self, task):
        self.all_project.append(task)

    def list_of_task(self):
        print(f"Проект магазина: {' '.join(self.all_project)}")

class ProjectTender():
    def __init__(self):
        self.all_project = []

    def add(self, task: Any):
        self.all_project.append(task)

    def list_of_task(self):
        print(f"Проект Тендера: {','.join(self.all_project)}")


class DirectorCompany():

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: Manager):
        self._builder = builder


    def easy_project(self):
        self._builder.get_task()
        self._builder.sell()
        self._builder.implement()

    def all_inclusive(self):
        self._builder.get_task()
        self._builder.visual_project()
        self._builder.sell()
        self._builder.implement()
        self._builder.do_document()

if __name__ == '__main__':
    director = DirectorCompany()
    builder = ShopManager()
    director.builder = builder

    print('Легкая продажа - это:')
    director.easy_project()
    builder.project.list_of_task()
    print('<<-->>' * 20)

    print('Продажа все включено это:')
    director.all_inclusive()
    builder.project.list_of_task()
    print('<<-->>' * 20)

    print('Обычно, продажа без директора это:')
    builder.get_task()
    builder.visual_project()
    builder.false_sales()
    builder.project.list_of_task()
    print('<<-->>' * 20)


    director2 = DirectorCompany()
    builder2 = TenderManager()
    director2.builder = builder2
    print('Обычно, тендер проходит так:')
    director2.all_inclusive()
    builder2.project.list_of_task()
    print('<<-->>' * 20)
    print('Но иногда так:')
    builder2.get_task()
    builder2.visual_project()
    builder2.false_sales()
    builder2.project.list_of_task()

