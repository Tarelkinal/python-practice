"""
    Создать класс Store. Поля: название магазина, адрес, коллекция аудиодисков (список экземпляров класса Audio),
    коллекция фильмов (список экземпляров класса DVD).
    Определить конструктор.
    Переопределить метод преобразования в строку для печати всей информации о магазине (с использованием переопределения в классах Audio и DVD).
    Переопределить методы получения количества дисков функцией len, получения диска по индексу, изменения по
    индексу, удаления по индексу (пусть вначале идут индексы аудиодисков, затем фильмов). Переопределить
    операции + и - для добавления или удаления диска. Добавить функцию создания txt-файла и записи всей
    информации в него (в том числе списков песен и главных ролей фильма).
"""
from Audio import Audio
from DVD import DVD

class Store:
    def __init__(self, mag_name = "None", address = "None", audiokol = [], filmkol = []):
        self.address = address
        self.mag_name = mag_name
        self.audiokol = audiokol
        self.filmkol = filmkol


    def __add__(self, other):
        if type(other) == Audio:
            self.audiokol.append(other)
        elif type(other) == DVD:
            self.filmkol.append(other)


    def __str__(self):
        res = ""
        for e in self.filmkol:
            res += '\n' + (str(e))
        for e in self.audiokol:
            res += '\n' + (str(e))
        return res + '\n'


    def __len__(self):
        # Переопределить методы получения количества дисков функцией len
        return len(self.audiokol) + len(self.videokol)


    def __getitem__(self, n):
        #Переопределить методы получения количества получения диска по индексу
        if len(self.audiokol) >= n+1:
            return self.DVD[n]

    def __setitem__(self, n, value):
        #Переопределить метод изменения по индексу
        if len(self.audiokol) >= n + 1 and type(value) == Drink:
            self.drinks[n] = value
        elif len(self.drinks) + len(self.food) <= n + 1 and type(value) == Food:
            self.food[n - len(self.drinks)] = value

    def write_into_file(self):
        f = open(self.name + '.txt', 'w')
        f.write(self.name + '\n' + self.adress + '\n')
        f.write('Магазин:\n')
        i = 1
        f.write('Музыка:\n')
        for audio in self.audiokol:
            f.write(str(i) + '. ' + str(audio))
            f.write('\n' + audio.get_composition())
            i += 1
        f.write('Фильмы:\n')
        for video in self.videokol:
            f.write(str(i) + '. ' + str(video))
            f.write('\n' + video.get_composition())
            i += 1
        f.close()


"""
def __len__(self):
    logger("INF", "выполнено получение длины меню")
    Переопределить метод получения количества пунктов меню функцией len
    return len(self.drinks) + len(self.food)

def __getitem__(self, n):
    logger("INF", "выполнено получение индекса")
    Переопределить метод получения напитка/блюда по индексу
    if len(self.drinks) >= n+1:
        return self.drinks[n]
    elif len(self.drinks) + len(self.food) >= n+1:
        return self.food[n - len(self.drinks)]


def __setitem__(self, n, value):
    logger("INF", "выполнено изменение по индексу")
    Переопределить метод изменения по индексу
    if len(self.drinks) >= n + 1 and type(value) == Drink:
        self.drinks[n] = value
    elif len(self.drinks) + len(self.food) <= n + 1 and type(value) == Food:
        self.food[n - len(self.drinks)] = value


def __delitem__(self, n):
    logger("INF", "пункт меню удален")
  Переопределить метод удаления по индексу (пусть вначале идут индексы напитков, затем горячих блюд).
    if len(self.drinks) >= n + 1:
        self.drinks.pop(n)
    else:
        self.food.pop(n - len(self.drinks))
"""

def make_test():
    m = Store("Mvideo", "ABC street")
    f1 = DVD("Im dragons", "Alternative rock", 200, "Apple", {"Britney": "Spears","Ed":"Boon"}, "Timur")
    m + f1
    print(str(m))


make_test()