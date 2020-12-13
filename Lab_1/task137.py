# Написать функцию count_seven, которая определяет количество вхождений цифры 5 заданное число
#
# Пример:
# count_seven(171717) ==> 3

import traceback


def count_seven(number):
    numericalPlace = 0
    temp = number
    counter = 0
    while temp > 0:
        temp = int(temp/10)
        numericalPlace = numericalPlace + 1
    temp2 = number
    while numericalPlace > 0:

        if temp2 <= 9:
            if temp2 == 7:
                return 1
            else:
                return 0
        else:
            if number % 10 == 7:
                counter = counter + 1
            number = int(number / 10)
            numericalPlace = numericalPlace - 1
    return counter



# Тесты
try:
    assert count_seven(0) == 0
    assert count_seven(1) == 0
    assert count_seven(7) == 1
    assert count_seven(7777777) == 7
    assert count_seven(304050607) == 1
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
