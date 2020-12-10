"""Создать производный от Disk класс Audio. Новые поля: исполнитель, студия звукозаписи, список песен (словарь вида
    название песни: длительность).
Определить конструктор, с вызовом родительского конструктора. Определить
    функции добавления новой песни, удаления песни, форматированной печати плейлиста.
Переопределить метод преобразования в строку для печати основной информации (исполнитель, название альбома, жанр,
    студия звукозаписи, цена)
"""

from Disk import Disk
class Audio(Disk):# Создать производный от Disk класс Audio
    def __init__(self, name="None", genre="None", price=0, performer = "None", album = "None", studio = "None", playlist = {}):  # Определить конструктор
        super().__init__(name, genre, price)  # с вызовом родительского конструктора.
        self.playlist = playlist
        self.studio = studio
        self.album = album
        self.performer = performer

    def __str__(self):
        return f"{super().__str__()}\n" + \
               f"Исполнитель: {self.performer}\n" + \
               f"Название альбома: {self.album}\n" + \
               f"Студия: {self.studio}\n"


    def addSong(self, name, performer, duration):
        self.name = name
        self.performer = performer
        self.duration = duration

    def removeSong(self, name):  # Определить функции изменения водителя
        self.name = name

    def formatPlaylist(self, playlist):
        self.playlist = playlist


# def make_test():
#     tc = Truck("Volga", 2, 2012, 1400, "Igor", "Pavlov",
#               {
#                    "Weels": 21,
#                    "Tank": 420,
#                    "Car toy": 1,
#                })
#     assert tc.maxCarryingCapacity == 1400
#     assert tc.driverName + ' ' + tc.driverSurname == "Igor Pavlov"
#     print(tc.driverName + ' ' + tc.driverSurname )
#     tc.addLoad("Gold ring", 2)
#     tc.deleteLoad("Weels")
#     assert str(tc) == "Марка: Volga\nМощность: 2\nГод: 2012\nМаксимальная грузоподъемность: 1400\nФИ водителья: Igor Pavlov"
#     tc.changeDriver('Oleg', 'Dundkin')
#     assert tc.driverName + ' ' + tc.driverSurname == "Oleg Dundkin"
#     assert str(tc) == "Марка: Volga\nМощность: 2\nГод: 2012\nМаксимальная грузоподъемность: 1400\nФИ водителья: Oleg Dundkin"
#     print("Тест пройден")
#
# make_test()