class Disk:
    def __init__(self, name, genre, price):
        self.DiskName = name
        self.DiskGenre = genre
        self.DiskPrice = price

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
