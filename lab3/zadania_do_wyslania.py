from PIL import Image
import numpy as np
from random import randrange

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)
pionowe_szare = rysuj_pasy_pionowe_szare(200,100, 1,10)
pionowe_szare.show()
# pionowe_szare.save('pasy_pion_szare.png')
def rysuj_ramki_szare(w, h, grub):
    tab = np.ones((h,w), dtype=np.uint8)
    ile = min(h,w) // (grub * 2)
    for i in range(0, ile):
        kolor_ramki = randrange(0, 256)
        top = i * grub
        bottom = h - top
        left = i * grub
        right = w - left
        tab[top:top + grub, left:right] = kolor_ramki
        tab[bottom - grub:bottom, left:right] = kolor_ramki
        tab[top:bottom, left:left + grub] = kolor_ramki
        tab[top:bottom, right - grub:right] = kolor_ramki
    return Image.fromarray(tab)

ramki = rysuj_ramki_szare(300, 200, 5)
ramki.show()
# ramki.save('ramki_szare.png')

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

def rysuj_po_skosie_szare(h,w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


def negatyw(obraz):
    tryb = obraz.mode
    tab = np.asarray(obraz)
    if tryb == '1':
        tab_neg = 1-tab.astype(np.uint8)
        return Image.fromarray(tab_neg * 255)
    elif tryb == 'L' or tryb == 'RGB':
        tab_neg = 255 - tab
        return Image.fromarray(tab_neg)

gwiazdka = Image.open("gwiazdka.bmp")
kolorowe = rysuj_ramki_kolorowe(200,[20,120,220],6, 5, -6)
im_skos = rysuj_po_skosie_szare(100, 300, 6, 5)
negatyw(gwiazdka).show()
negatyw(im_skos).show()
negatyw(kolorowe).show()

# kolorowe.save('ramki_kolorowe.png')
# im_skos.save('im_skos.png')
# negatyw(gwiazdka).save('gwiazdka_negatyw.png')
# negatyw(im_skos).save('im_skos_negatyw.png')
# negatyw(kolorowe).save('ramki_kolorowe_negatyw.png')

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
inicjaly_paski.show()
# inicjaly_paski.save('inicjaly_kolorowe.jpg')
# inicjaly_paski.save('inicjaly_kolorowe.png')
