from textwrap import dedent

from Lab_3.Disk import Disk
from Lab_3.logger import logging


class DVD(Disk):
    def __init__(self, name, genre, price, company, producer):
        super().__init__(name, genre, price)
        self.producer = producer
        self.main_roles = {}
        self.company = company
        logging('CRE', 'создан', self.__repr__())

    def __str__(self):
        return f"{super().__str__()}\n" + \
               f"Режиссер: {self.producer}\n" + \
               f"Кинокомпания: {self.company}\n"

    def change_producer(self, producer):
        self.producer = producer
        logging('INF', 'изменен режиссер', f'updated value: {producer}')

    def add_roles(self, role, name):
        self.main_roles[role] = name
        logging('INF', 'добавлена/изменена роль', f'updated value: {role} -- {name}')

    def del_roles(self, role):
        try:
            self.main_roles.pop(role)
            logging('INF', 'удалена роль', f'deleted value: {role}')
        except KeyError:
            logging('ERR', 'данная роль не найдена в списке', f'{role}')


def make_test():
    a = DVD('New DVD', 'romance', 505, 'WB', 'Rose Smith')
    true_dvd_represent = dedent("""\
        Название: New DVD
        Жанр: romance
        Цена: 505
        Режиссер: Rose Smith
        Кинокомпания: WB
    """)

    assert true_dvd_represent == str(a)

    a.change_producer('Will Turner')
    assert a.producer == 'Will Turner'

    a.add_roles('main', 'Elizabet Torn')
    assert 'main' in a.main_roles.keys()
    assert a.main_roles['main'] == 'Elizabet Torn'

    a.del_roles('main')
    assert 'main' not in a.main_roles.keys()


if __name__ == '__main__':
    make_test()
