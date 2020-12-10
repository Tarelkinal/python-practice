# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback


def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]


def palindrome(num):
    mas = createmas(num)
    res = []
    split1, split2 = split_list(mas)
    split11, split12 = split1
    split21, split22 = split2
    if split11 == split12.reverse():
        res.append(split11 + split12)


    return res


def checkfour(fourmas):
    res = []
    if fourmas[0] == fourmas[3]:
        res.append(fourmas[0] + fourmas[3])
    print(res)


def createmas(num):
    res = []
    for i in range(len(num)):
        res.append(num % 10)
        num = int(num/10)
    res.reverse()
    return res

# Тесты
try:
    assert palindrome(1551) == [55, 1551]
    assert palindrome(221122) == [11, 22, 2112, 221122]
    assert palindrome(10015885) == [88, 1001, 5885]
    assert palindrome(13598) == []
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")