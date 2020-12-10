# Написать функцию palindrome, которая для заданного числа num возвращает список всех числовых палиндромов,
# содержащихся в каждом номере. Массив должен быть отсортирован в порядке возрастания,
# а любые дубликаты должны быть удалены.
#
# Пример:
# palindrome(34322122)  =>  [22, 212, 343, 22122]


import traceback


def palindrome(num: int) -> list:
    res = []
    str_num = str(num)

    for i in range(len(str_num) - 1):
        for j in range(i + 2, len(str_num) + 1):

            temp_str_num = str_num[i: j]

            if is_palindrome(temp_str_num):
                res.append(int(temp_str_num))

    return sorted(list(set(res)))


def is_palindrome(str_num: str) -> bool:

    if not int(str_num):
        return False

    for i in range(len(str_num) // 2):

        if str_num[i] != str_num[len(str_num) - i - 1]:
            return False

    return True


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
