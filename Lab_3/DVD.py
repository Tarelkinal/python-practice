"""Создать производный от Disk класс DVD. Новые поля: режиссер, кинокомпания, главные роли (словарь вида роль: ФИ актера).
    Определить конструктор, с вызовом родительского конструктора. Определить функции изменения режиссера, добавления,
    удаления и изменения списка главных ролей. Переопределить метод преобразования в строку для печати основной
    информации (режиссер, название фильма, жанр, кинокомпания, цена).
"""

from Disk import Disk


class DVD(Disk):
    def __init__(self, name="None", genre="None", price=0, company="None", main_roles={}, producer="None"):
        super().__init__(name, genre, price)
        self.producer = producer
        self.main_roles = main_roles
        self.company = company

    def __str__(self):
        return f"{super().__str__()}\n" + \
               f"Режиссер: {self.producer}\n" + \
               f"Кинокомпания: {self.company}\n"

    def changeProducer(self, producer):
        self.producer = producer

    def addRoles(self, Name, Surname):
        self.main_roles.append(Surname, Name)
