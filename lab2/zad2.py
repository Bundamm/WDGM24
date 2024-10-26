from PIL import Image
import numpy as np

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
ramka = rysuj_ramki(80,130,5)
# ramka.save("ramka.bmp")
# ramka.show()
obrazek = Image.open("obraz.bmp")
mode = obrazek.mode
size = obrazek.size
value = obrazek
tablica = np.asarray(obrazek)
wymiar = tablica.shape
typ = tablica.dtype
pixel = np.asarray(obrazek)




obrazek2=Image.fromarray(tablica)
# obrazek2.show()
print("tryb:", mode, " wartość pikesla:", pixel[13,66], " wartość elem tablicy:", pixel[97,20])


def rysuj_pasy_pionowe(w,h,grub):
    t = (h, w)
    tab = np.ones(t,dtype=np.bool_)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    return Image.fromarray(tab)
obrazek = rysuj_pasy_pionowe(100,100, 5)
# obrazek.show()

def rysuj_wlasne(w,h,grub):
    tab = np.ones((h,w),dtype=np.bool_)
    tab[(h//2)-grub:grub+(h//2), :] = 0
    tab[:,(w//2)-grub:grub+(w//2)] = 0
    return Image.fromarray(tab)
krzyz = rysuj_wlasne(100,200,10)
krzyz.show()
krzyz.save("krzyz.bmp")