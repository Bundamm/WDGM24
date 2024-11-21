from PIL import Image
import numpy as np

obraz = Image.open("inicjaly.bmp")
print("tryb", obraz.mode)

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    tab_obraz[0:grub, :] = 0
    tab_obraz[-grub:h, :] = 0
    tab_obraz[:, 0:grub] = 0
    tab_obraz[:, -grub:w] = 0
    tab = tab_obraz.astype(np.bool_)
    return Image.fromarray(tab)
z_ramka = rysuj_ramke_w_obrazie(obraz,5)
z_ramka.show()

def rysuj_ramki(w,h,grub):
    tab = np.ones((h,w),dtype=np.bool_)
    ile = min(w, h) // (grub*2)
    for i in range(0,ile,2):
        top = i * grub
        bottom = h - top
        left = i * grub
        right = w - left
        tab[top:top+grub, left:right] = 0
        tab[bottom - grub:bottom, left:right] = 0
        tab[top:bottom, left:left + grub] = 0
        tab[top:bottom, right - grub:right] = 0
    return Image.fromarray(tab)
ramka = rysuj_ramki(500,300,10)
ramka.show()

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
obrazek = rysuj_pasy_pionowe(100,100, 5)
obrazek.show()

def rysuj_wlasne(w,h,grub):
    tab = np.ones((h,w),dtype=np.bool_)
    tab[(h//2)-grub:grub+(h//2), :] = 0
    tab[:,(w//2)-grub:grub+(w//2)] = 0
    return Image.fromarray(tab)
krzyz = rysuj_wlasne(100,100,10)
krzyz.show()

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
obraz_wstawianie = wstaw_obraz_w_obraz(obrazek, obraz, 0,25)
obraz_wstawianie.show()


