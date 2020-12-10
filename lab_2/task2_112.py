# Написать функцию case_sensitive, которая определяет все ли символы
# в заданной строке являются прописными и возвращает список из значения
# истинности и списка заглавных букв
#
# Примеры:
# case_sensitive("fgfgjjjg") ==> [True, []]
# case_sensitive("fgDfhghAgg") ==> [False, ['D', 'A']]

import traceback


def case_sensitive(s):
    out_str = ''
    for i in range(len(s)):
        if 64 < ord(s[i]) < 91:
            out_str = out_str + s[i]
    if out_str == '':
        out_str = out_str + 'True'
    else:
        out_str = out_str + 'False'

    return out_str


# Тесты
try:
    assert case_sensitive('asd'), [True, []]
    assert case_sensitive('cellS'), [False, ['S']]
    assert case_sensitive('z'), [True, []]
    assert case_sensitive(''), [True, []]
    assert case_sensitive('aaTRggjS'), [True, ['T', 'R', 'S']]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
