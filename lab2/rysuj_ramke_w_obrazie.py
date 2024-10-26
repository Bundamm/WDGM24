from PIL import Image
import numpy as np


t1 = np.loadtxt("tablica.txt", dtype=np.bool_)
obraz = Image.fromarray(t1)
def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    tab_obraz[0:grub, :] = 0
    tab_obraz[-grub:h, :] = 0
    tab_obraz[:, 0:grub] = 0
    tab_obraz[:, -grub:w] = 0
    tab = tab_obraz.astype(np.bool_)
    return Image.fromarray(tab)
z_ramka = rysuj_ramke_w_obrazie(obraz,20)
z_ramka.save("obraz.bmp")
