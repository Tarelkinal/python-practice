import os


def make_dir():
    struct = {'СЕМЕСТР 1': ['python', 'algorithms', 'math'],
              'СЕМЕСТР 2': ['C++', 'Java', 'physics']}

    for k in struct.keys():
        for v in struct[k]:
            cur_path = f'.\\УЧЕБА\\{k}\\{v}'
            os.makedirs(cur_path, exist_ok=True)
            path = os.path.join(os.getcwd() + cur_path)
            with open(f'{path}\\path.txt', 'w') as f_in:
                f_in.write(f'{path}\\path.txt')


if __name__ == '__main__':
    make_dir()
