import os
from pprint import pprint


def make_dirs():
    struct = {'СЕМЕСТР 1': ['python', 'algorithms', 'math'],
              'СЕМЕСТР 2': ['C++', 'Java', 'physics']}

    for k in struct.keys():
        for v in struct[k]:
            cur_path = f'.\\УЧЕБА\\{k}\\{v}'
            os.makedirs(cur_path, exist_ok=True)
            path = os.path.join(os.getcwd() + cur_path)
            with open(f'{path}\\path.txt', 'w') as f_in:
                f_in.write(f'{path}\\path.txt')


def get_dirs_dict(path=os.getcwd()):
    dir_li = [x for x in os.scandir(path) if x.is_dir()]
    files_li = [x for x in os.scandir(path) if x.is_file()]
    if not dir_li:
        if not files_li:
            return None
        else:
            result = files_li[0].name if len(files_li) == 1 else list(map(lambda x: x.name, files_li))
            return result

    if len(dir_li) == 1 and len(files_li) == 0:
        return {dir_li[0].name: get_dirs_dict(path + '\\' + '\\' + dir_li[0].name)}
    else:
        result = []
        for d in dir_li:
            result.append({d.name: get_dirs_dict(path + '\\' + d.name)})
        for f in files_li:
            result.append(f.name)
        return result


if __name__ == '__main__':
    pprint(get_dirs_dict())
