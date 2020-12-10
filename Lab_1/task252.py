# Написать функцию array_diff(a, b), которая возвращает разность списков a и b.
# Т.е. из спсика a должны быть удалены все значения, которые встречаются в списке b.
#
# Пример:
# array_diff([1,2,2,2,3],[2]) == [1,3]


import traceback


def array_diff(a, b):
    try:
        for j in range(len(a)):
            for i in range(len(b)):
                a.remove(b[i])
    except ValueError:
        i = 0
    return a


# Тесты
try:
    assert array_diff([1, 2, 3], [2]) == [1, 3]
    assert array_diff([2, 1, 3, 2, 1, 3, 3], [3, 1]) == [2, 2]
    assert array_diff([6, 5, 4, 3, 2, 1], []) == [6, 5, 4, 3, 2, 1]
    assert array_diff([6, 5, 4, 3, 3, 3, 3, 2, 1], [3]) == [6, 5, 4, 2, 1]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
