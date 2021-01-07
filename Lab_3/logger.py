from datetime import datetime


def logging(key, comment, obj):
    with open('logs.txt', 'a', encoding='cp1251') as f_in:
        f_in.write(f'{key} --- {datetime.now()} --- {comment} {str(obj)}\n')
