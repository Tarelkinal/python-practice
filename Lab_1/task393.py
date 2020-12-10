# Написать функцию расшифровки кода decode(code, key)
# Процесс шифрования: каждой букве латинского алфавита abcdefghijklmnopqrstuvwxyz
# последовательно ставится в соответствие число от 1 до 26.
# Дальше к каждому числу последовательно прибавляется цифры из ключа.
#
# Пример:
# слово: abcxyz, код: 4567 =>
# [a->1, b->2, c->3, x->24, y->25, z->26] =>
# [1 + 4, 2 + 5, 3 + 6, 24 + 7, 25 + 4, 26 + 5] => код: [5, 7, 8, 31, 29, 31]


import traceback


def decode(code, key):
    string = "abcdefghijklmnopqrstuvwxyz"
    sp_key = split_key(key)
    result = ""
    j = -1
    for i in range(len(code)):
        if j == len(sp_key)-1:
            j = 0
        else:
            j = j + 1
        temp = code[i]
        temp = temp - sp_key[j]
        result = result + string[temp-1]

    return result

def split_key(key):
    f = 0
    t = key
    while t > 0:
        t = int(t / 10)
        f = f + 1
    res = []
    for i in range(f):
        res.append(key % 10)
        key = int(key / 10)
    res.reverse()
    return res


# Тесты
try:
    assert decode([20, 12, 18, 30, 21], 1939) == "scout"
    assert decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939) == "masterpiece"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
