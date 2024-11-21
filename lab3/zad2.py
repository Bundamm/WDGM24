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

# kolor = rysuj_ramki_kolorowe(200, [20, 120,220], 10, 10, 10)
# kolor.show()

def rysuj_po_skosie_szare(h, w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w)  # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)


skos = rysuj_po_skosie_szare(20, 30, 1, 3)
# skos.show()
def negatyw(obraz):
    mode = obraz.mode
    tab = np.asarray(obraz)
    if mode == '1':
        tab_neg = 1-tab
        return Image.fromarray(tab_neg)
    elif mode == 'L' or mode == 'RGB':
        tab_neg = 255 - tab
        return Image.fromarray(tab_neg)



# negatywny = negatyw(pionowe_szare)
# negatywny.show()
# kolor_n = negatyw(kolor)
# kolor_n.show()
# skos_n = negatyw(skos)
# skos_n.show()

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
print(ramki.mode)
# ramki.save('ramki_szare.png')


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
pasy_pion = rysuj_pasy_pionowe_szare(300,200,5,10)
# pasy_pion.save('pasy_pion_szare.png')