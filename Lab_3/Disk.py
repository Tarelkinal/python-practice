#Создать класс Disk с полями название, жанр, цена. Добавить конструктор класса.

class Disk:
    def __init__(self, name="None", genre="None", price=0):  # Добавить конструктор класса.
        self.DiskName = name  # название
        self.DiskGenre = genre  # жанр
        self.DiskPrice = price  # цена

    def __str__(self):
        return f"Название: {self.DiskName}\n" + \
               f"Жанр: {self.DiskGenre}\n" + \
               f"Цена: {self.DiskPrice}"


def make_test():
    c = Disk("DubStepper", "Dubstep", 500)
    assert c.DiskName == "DubStepper"
    assert c.DiskGenre == "Dubstep"
    assert c.DiskPrice == 500
    assert str(c) == "Название: DubStepper\nЖанр: Dubstep\nЦена: 500"
    print("Тест пройден")


make_test()