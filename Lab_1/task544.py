# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.


cars = [{"id": 123456, "model": "Mercedes-Benz", "year": 2019, "color": "red", "class": "sedan", "cost": "5 680 000 Р"},
        {"id": 654321, "model": "Lada", "year": 1978, "color": "green", "class": "sedan", "cost": "130 000 Р"},
        {"id": 123321, "model": "Volvo", "year": 2013, "color": "silver", "class": "sedan", "cost": "750 000 Р"},
        {"id": 321123, "model": "Subaru", "year": 2005, "color": "black", "class": "sedan", "cost": "1 600 000 Р"},
        {"id": 987654, "model": "BMV", "year": 2010, "color": "purple-black", "class": "sedan", "cost": "2 300 000 Р"}]


def print_every_car(mas):
    for i in range(len(mas)):
        print(str(mas[i]["id"])
              + " " + str(mas[i]["model"])
              + " " + str(mas[i]["year"])
              + " " + str(mas[i]["color"])
              + " " + str(mas[i]["class"])
              + " " + str(mas[i]["cost"]))


def print_сar(mas):
    print("Введите номер машины: ")
    x = int(input())
    for i in range(len(mas)):
        if mas[i]["id"] == x:
            print(str(mas[i]["id"])
                  + " " + str(mas[i]["model"])
                  + " " + str(mas[i]["year"])
                  + " " + str(mas[i]["color"])
                  + " " + str(mas[i]["class"])
                  + " " + str(mas[i]["cost"]))


def car_out_by_year(mas):
    l = 0
    print("Введите год: ")
    x = int(input())
    for i in range(len(mas)):
        if cars[i]["year"] > x:
            l += 1
    print("Количество машин: ", l)


def car_update(mas):
    print("Введите номер автомобителя: ")
    x = int(input())
    for i in range(len(mas)):
        if cars[i]["id"] == x:
            cars[i]["model"] = input()
            cars[i]["year"] = int(input())
            cars[i]["color"] = input()
            cars[i]["class"] = input()
            cars[i]["cost"] = input()
    print("Обновленная информация: ")
    for i in range(len(mas)):
        print(str(mas[i]["id"])
              + " " + str(mas[i]["model"])
              + " " + str(mas[i]["year"])
              + " " + str(mas[i]["color"])
              + " " + str(mas[i]["class"])
              + " " + str(mas[i]["cost"]))


def car_delete(mas):
    x = int(input())
    for i in range(len(mas)):
        if cars[i]["id"] == x:
            k = i
    mas.remove(mas[k])
    for i in range(len(mas)):
        print(str(mas[i]["id"])
              + " " + str(mas[i]["model"])
              + " " + str(mas[i]["year"])
              + " " + str(mas[i]["color"])
              + " " + str(mas[i]["class"])
              + " " + str(mas[i]["cost"]))


print("""Выберите действие: 
– вывода информации о всех машинах;
– вывода информации о всех машинах – вывода информации о машине по введенному с клавиатуры номеру
– вывода количества машин, моложе введённого года
– обновлении всей информации о машине по введенному номеру
– удалении машины по номеру""")

l = int(input(""))
if l == 1:
    print_every_car(cars)
if l == 2:
    print_сar(cars)
if l == 3:
    car_out_by_year(cars)
if l == 4:
    car_update(cars)
if l == 5:
    car_delete(cars)
