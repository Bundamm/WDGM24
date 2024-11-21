from PIL import Image
import numpy as np
from random import randrange



def koloruj_w_paski(obraz, grub, liczba_kolorow):
    t_obraz = np.asarray(obraz)
    h,w = t_obraz.shape
    tab = np.ones((h,w,3),dtype=np.uint8) * 255
    kolory = [[]] * liczba_kolorow
    for l in range(liczba_kolorow):
        kolory[l] = [randrange(0, 256), randrange(0, 256), randrange(0, 256)]
    for i in range(h):
        ile = len(kolory)
        kolor = kolory[(i//grub) % ile]
        for j in range(w):
            if t_obraz[i,j] == False:
                tab[i,j] = kolor
    return Image.fromarray(tab, mode='RGB')
obrazek = Image.open("inicjaly.bmp")
inicjaly_paski = koloruj_w_paski(obrazek, 5, 10)
# inicjaly_paski.save('inicjaly_kolorowe.jpg')
# inicjaly_paski.save('inicjaly_kolorowe.png')