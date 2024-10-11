from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")
print("tryb", obraz.mode)

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h,w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w-grub,w):
            tab_obraz[i][j] = 0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h-grub, h):
            tab_obraz[j][i] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)
z_ramka = rysuj_ramke_w_obrazie(obraz,5)
# z_ramka.show()


def rysuj_pasy_pionowe(w,h,grub):
    return
def rysuj_ramki(w,h,grub):
    return
def rysuj_wlasne(w,h,x):
    return
def wstaw_obraz(w,h,m,n,obraz):
    return
