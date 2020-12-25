import re
from collections import Counter
"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя метод format
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  и не делить слова.
"""
NEW_FILE = 'new_file.txt'
WIKIPEDIA_FILE_PATH = 'wikipedia.txt'


def wiki_function():
    with open(WIKIPEDIA_FILE_PATH, 'r') as f_in:
        lines_li = []
        for x in f_in.readlines():
            if x.strip():
                lines_li.append(' '.join(re.findall(r'[A-Za-z]+', x.strip())))

        text = ' '.join(lines_li)
        words_cnt_dict = Counter(text.split())
        top_10_words = words_cnt_dict.most_common(10)
        for i in range(len(top_10_words)):
            print('{} place --- {} --- {} times'.format(i + 1, top_10_words[i][0], top_10_words[i][1]))
            text = re.sub(f'\\b{top_10_words[i][0]}\\b', 'PYTHON', text)
            print(1)

        with open(NEW_FILE, 'w') as f_out:
            counter = 0
            for word in text.split():
                if counter + word.__len__() > 100:
                    counter = 0
                    f_out.write('\n')

                counter += word.__len__() + 1
                f_out.write(word + ' ')


if __name__ == "__main__":
    wiki_function()
