from Lab_3.Audio import Audio
from Lab_3.DVD import DVD


class Store:
    def __init__(self, shop_name, address):
        self.address = address
        self.shop_name = shop_name
        self.audio_col = []
        self.film_col = []

    def __add__(self, other):
        if type(other) == Audio:
            self.audio_col.append(other)
        elif type(other) == DVD:
            self.film_col.append(other)

    def __sub__(self, other):
        if type(other) == Audio:
            for audio in self.audio_col:
                if str(audio) == str(other):
                    self.audio_col.remove(audio)
                    break
        elif type(other) == DVD:
            for dvd in self.film_col:
                if str(dvd) == str(other):
                    self.film_col.remove(dvd)

    def __str__(self):
        res = f'shop name: {self.shop_name}, shop address: {self.address}\n'

        res += 'films presented:\n'
        for film in self.film_col:
            res += str(film)

        res += 'audio presented:\n'
        for audio in self.audio_col:
            res += str(audio)

        return res

    def __len__(self):
        return len(self.audio_col) + len(self.film_col)

    def __getitem__(self, i):
        if i < len(self.audio_col):
            return self.audio_col[i]
        else:
            return self.film_col[i - len(self.audio_col)]

    def __setitem__(self, i, new_obj):
        try:
            if i < len(self.audio_col):
                if type(new_obj) != Audio:
                    raise ValueError
                self.audio_col[i] = new_obj
            else:
                if type(new_obj) == Audio:
                    raise ValueError
                self.film_col[i - len(self.audio_col)] = new_obj
        except ValueError:
            print('ERR')

    def write_into_file(self):
        with open(f'{self.shop_name}.txt', 'w', encoding='cp1251') as f_out:
            f_out.write(self.__str__())


def make_test():
    store = Store('DVD and Audio shop', '5 Avenue 31')
    new_audio = Audio('New disk', 'rock', 505, 'Mike Stallone', 'new album', 'covers io')
    new_dvd = DVD('New DVD', 'romance', 505, 'WB', 'Rose Smith')

    store + new_audio
    store + new_dvd

    assert len(store) == 2

    store - Audio('New disk', 'rock', 505, 'Mike Stallone', 'new album', 'covers io')
    assert len(store) == 1
    assert len(store.audio_col) == 0
    assert str(store[0]) == str(new_dvd)

    new_dvd_2 = DVD('Another new DVD', 'romance', 505, 'WB', 'Rose Smith')
    store[0] = new_dvd_2
    assert str(store[0]) == str(new_dvd_2)

    store.write_into_file()
    with open('DVD and Audio shop.txt', 'r', encoding='cp1251') as f_in:
        assert f_in.read() == str(store)


if __name__ == '__main__':
    make_test()
