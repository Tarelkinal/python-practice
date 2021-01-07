from textwrap import dedent

from Lab_3.Disk import Disk
from Lab_3.logger import logging


class Audio(Disk):
    def __init__(self, name, genre, price, performer, album, studio):
        super().__init__(name, genre, price)
        self.playlist = {}
        self.studio = studio
        self.album = album
        self.performer = performer
        logging('CRE', 'создан', self.__repr__())

    def __str__(self):
        return f"{super().__str__()}\n" + \
               f"Исполнитель: {self.performer}\n" + \
               f"Название альбома: {self.album}\n" + \
               f"Студия: {self.studio}\n"

    def add_song(self, name, duration):
        self.playlist[name] = duration
        logging('INF', 'добавлен трек в playlist', f'{name}: {duration}')

    def remove_song(self, name):
        try:
            self.playlist.pop(name)
            logging('INF', 'удален трек из playlist', f'{name}')
        except KeyError:
            logging('ERR', 'трек не найден в playlist', f'{name}')

    def format_print(self):
        res = ''
        for k, v in self.playlist.items():
            res += f'name: {k}, duration: {v}'
        print(res)
        logging('INF', 'распечатан', self.__repr__())
        return res


def make_test():
    a = Audio('New disk', 'rock', 505, 'Mike Stallone', 'new album', 'covers io')
    true_audio_represent = dedent("""\
        Название: New disk
        Жанр: rock
        Цена: 505
        Исполнитель: Mike Stallone
        Название альбома: new album
        Студия: covers io
    """)
    true_format_playlist_print = 'name: new song, duration: 5.32'

    a.add_song('new song', 5.32)

    assert true_audio_represent == str(a)
    assert true_format_playlist_print == a.format_print()
    assert 'new song' in a.playlist.keys()
    assert a.playlist['new song'] == 5.32

    a.remove_song('new song')
    assert 'new song' not in a.playlist.keys()


if __name__ == '__main__':
    make_test()
