from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")
print("tryb", obraz.mode)

def rysuj_pasy_pionowe(w,h,grub):
    t = (h, w)
    tab = np.ones(t,dtype=np.bool_)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    return Image.fromarray(tab)
obrazek = rysuj_pasy_pionowe(300,200, 15)



def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany,m,n):
    tab_obraz_bazowy = np.asarray(obraz_bazowy).astype(np.int_)
    h0, w0 = tab_obraz_bazowy.shape
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)
    h, w = tab_obraz_wstawiany.shape
    n_k = min(h0, n + h)
    m_k = min(w0, m + w)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_bazowy[i][j] = tab_obraz_wstawiany[i-n][j-m]
    tab_obraz_bazowy = tab_obraz_bazowy.astype(bool)
    return Image.fromarray(tab_obraz_bazowy)
obraz_wstawianie = wstaw_obraz_w_obraz(obrazek, obraz, 250,100)
obraz_wstawianie2 = wstaw_obraz_w_obraz(obrazek, obraz, 0,50)
obraz_wstawianie.save("obrazek1.bmp")
obraz_wstawianie2.save("obrazek2.bmp")



