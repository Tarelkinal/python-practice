import re

test = """ 1.2
 1.
   1.0e-55
    e-12
6.5E
1e-12
+4.1234567890E-99999
7.6e+12.5
99"""


def real_number(number_str: str):
    answer = re.findall(r'\S+', number_str)[0]
    if re.fullmatch(r'\s*[+-]?\d+(?:\.\d+[eE][+-]?\d+|\.\d+|[eE][+-]?\d+)\s*', number_str):
        print(f'{answer} is legal')
    else:
        print(f'{answer} is illegal')


def make_test():
    test_numbers = test.split('\n')
    for number_str in test_numbers:
        real_number(number_str)


if __name__ == '__main__':
    make_test()
