import pickle

from Lab_3.Store import Store
from Lab_3.Audio import Audio
from Lab_3.DVD import DVD


if __name__ == '__main__':
    with open('store_dump.pkl', 'rb') as f_in:
        store = pickle.load(f_in)

    print(store)

    new_audio = Audio('New disk', 'rock', 505, 'Mike Stallone', 'new album', 'covers io')
    new_dvd = DVD('New DVD', 'romance', 505, 'WB', 'Rose Smith')

    store + new_audio
    store + new_dvd

    assert len(store) == 3

    store - Audio('New disk', 'rock', 505, 'Mike Stallone', 'new album', 'covers io')
    assert len(store) == 2
    assert len(store.audio_col) == 0
