from PIL import Image
import numpy as np
from random import randrange
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

obrazek = Image.open("inicjaly.bmp")
mode = obrazek.mode
format = obrazek.format
size = obrazek.size
print("tryb:", mode, " format:", format, " rozmiar:", size)

dane_obrazka = np.asarray(obrazek)
do = dane_obrazka.astype(np.uint8)
print(do)


t1_text = open('t1.txt', 'w')
for rows in do:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')
t1_text.close()

dane1 = do[8][14]
print(dane1)

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

#1
im = Image.open('im.png')
# print(im.size)
# print(im.mode)
#2
T = np.array(im)
t_r = T[:,:,0]
im_r = Image.fromarray(t_r)
t_g = T[:,:,1]
im_g = Image.fromarray(t_g)
t_b = T[:,:,2]
im_b = Image.fromarray(t_b)
im1 = Image.merge('RGB', (im_r, im_g, im_b))
porownanie = ImageChops.difference(im,im1)
plt.figure(figsize=(4,2))
plt.subplot(1,3,1)
plt.imshow(im)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(porownanie)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
# plt.show()
im1.save('im1.png')
#3
r,g,b = im.split()
im2 = Image.merge('RGB', (b, g, r))
# im2.save("im2.jpg")
# im2.save("im2.png")
im2_1 = Image.open('im2.jpg')
im2_2 = Image.open('im2.png')
dif = ImageChops.difference(im2_2, im2_2)
# dif.show()
#Prawie czarny obraz zatem różnią się delikatnie
plt.figure(figsize=(40,10))
plt.subplot(1,3,1)
plt.imshow(im2_1)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im2_2)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(dif)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
# plt.show()
# Obrazy są prawie takie same ale różnią minimalnie przez kompresję JPEG głównie przy środku są bardzo podobne ale nie co do pixela
#4
def sprawdz_czym_sie_rozni(obraz, mix):
    obraz_t = np.asarray(obraz)
    mix_t = np.asarray(mix)
    if obraz_t.shape != mix_t.shape:
        return "Nie są to te same obrazy jako że mają różny kształt"
    if np.array_equal(obraz_t, mix_t):
        return "Obrazy są takie same"
    negated = 255 - obraz_t
    if (np.array_equal(negated, mix_t)):
        return "Mix jest negatywem oryginalnego obrazu."
    permutations = [
        (0, 1, 2),  # RGB
        (0, 2, 1),  # RBG
        (1, 0, 2),  # GRB
        (1, 2, 0),  # GBR
        (2, 0, 1),  # BRG
        (2, 1, 0)  # BGR
    ]
    for perm in permutations:
        # Tworzymy obraz oryginalny z przestawionymi kanałami zgodnie z permutacją
        obraz_kanaly = obraz_t[:, :, list(perm)]

        # Sprawdzamy, czy przestawione kanały oryginału odpowiadają kanałom obrazu mix
        if np.array_equal(obraz_kanaly, mix_t):
            return f"Zamiana kanałów: {perm}"
    return "Jeszcze inne różnice"

def negatyw(obraz):
    tryb = obraz.mode
    tab = np.asarray(obraz)
    if tryb == '1':
        tab_neg = 1-tab.astype(np.uint8)
        return Image.fromarray(tab_neg * 255)
    elif tryb == 'L' or tryb == 'RGB':
        tab_neg = 255 - tab
        return Image.fromarray(tab_neg)

m310 = Image.open('mix310.png')
o10 = Image.open('obraz10.jpg')

print(sprawdz_czym_sie_rozni(o10,m310))

#5
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
w, h = im.size
im3 = rysuj_ramki_szare(w, h, 5)


im3_1 = Image.merge('RGB', (r, im3, b))
im3_2 = Image.merge('RGB', (im3, g, b))
im3_3 = Image.merge('RGB', (r, g, im3))
plt.figure(figsize=(40,10))
plt.subplot(1,3,1)
plt.imshow(im3_1)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im3_2)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(im3_3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()
# plt.savefig('fig4.png')

#6
def rysuj_histogram(obraz):
    plt.figure(figsize=(40,10))
    plt.subplot(1,3,1)
    hist = obraz.histogram()
    plt.bar(range(256), hist[:256], color='r')
    plt.subplot(1,3,2)
    plt.bar(range(256), hist[256:2 * 256], color='g')
    plt.subplot(1,3,3)
    plt.bar(range(256), hist[2*256:], color='b')
    plt.show()
# plt.show()
# print("Jest dokładnie: " ,g.histogram()[1], "pikseli koloru 1 na kanale g")

#7
def sprawdz_czy_rowne(obraz1, obraz2):
    # Sprawdzam czy mają taką samą wielkość i tryb
    identyczne = obraz1.mode == obraz2.mode and obraz1.size == obraz2.size
    if identyczne:
        diff_im = ImageChops.difference(obraz1, obraz2)
        diff_t = np.asarray(diff_im).copy()
        diff_pix = np.count_nonzero(diff_t)
        black = (diff_t[:, :, 0] <= 10) & (diff_t[:, :, 1] <= 10) & (diff_t[:, :, 2] <= 10) # Sprawdzam miejsca gdzie piksele są blisko kolorem czarnego
        diff_t[black] = [255,255,255] # i zamieniam je na biały żeby było dobrze widać miejsca gdzie są różnice
        diff_im = Image.fromarray(diff_t)
         # Liczę niezerowe piksele w tablicy obrazu wykonanego przez difference
        diff_im.show()

        return diff_pix
    else:
        diff_pix = None
        return diff_pix

print(sprawdz_czy_rowne(im2_1,im2_2))
# o9 = Image.open('obraz9.jpg')
# hist = o9.histogram()
# plt.bar(range(256), hist[2*256:], color='b')
# plt.savefig("hist.png")

# print(o9.histogram()[100])
# blue_channel = o9.getchannel(2)  # Blue channel
# blue_data = np.asarray(blue_channel)
# pixel_count_blue_value_100 = np.sum(blue_data == 100)
# print(pixel_count_blue_value_100)


# print("Ilość różnych pikseli: ", sprawdz_czy_rowne(im2_1, im2_2))
#8
# print(Image.open('beksinski1.png').mode)
# Dzieje się tak dlatego, że beksinski1 ma jeszcze 4 kanał alfa

#1
ini = Image.open('inicjaly.bmp')
baz = Image.open('obraz.png')
def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    if obraz_wstawiany.mode != '1':
        return "Nieprawidłowy tryb obrazu wstawianego"
    np_baza = np.asarray(obraz_bazowy).astype(np.int_)
    h0, w0, c = np_baza.shape
    np_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)
    h,w = np_wstawiany.shape
    n_k = min(h0, n+h)
    m_k = min(w0, m+w)
    n_p = max(0,n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p,m_k):
            if np_wstawiany[i-n, j-m] == 0:
                np_baza[i][j] = kolor
    return Image.fromarray(np_baza.astype(np.uint8))
obraz1 = wstaw_inicjaly(baz, ini, baz.width - ini.width, 0, [255, 0, 0])  # Prawy górny róg
obraz2 = wstaw_inicjaly(obraz1, ini, 0, baz.height - ini.height, [255, 255, 0])             # Lewy dolny róg
obraz3 = wstaw_inicjaly(obraz2, ini, baz.width - ini.width// 2, baz.height // 2, [0, 0, 255])    # Środek wysokości


obraz3.save('obraz_inicjaly.png')
obraz3
#2
obraz = Image.open("obraz.png")
obraz.save("obraz1.jpg")

for i in range(1, 5):
    img = Image.open(f"obraz{i}.jpg")
    img.save(f"obraz{i + 1}.jpg")

# Różnice między oryginałem i obraz5

obraz = Image.open("obraz.png")
obraz5 = Image.open("obraz5.jpg")


# Różnice między obrazami
roznica = ImageChops.difference(obraz, obraz5)

# Statystyki różnicy
roznica_np = np.array(roznica)
def statystyki(im):
    s = stat.Stat(im)
    print("średnia ", s.mean)  # srednia
    print("mediana ", s.median)  # mediana
    print("odchylenie standardowe ", s.stddev) # odchylenie standardowe
statystyki(roznica)


# Histogramy obrazów i różnicy
fig, axs = plt.subplots(3, 2, figsize=(12, 8))
axs[0, 0].imshow(obraz)
axs[0, 0].set_title("Oryginalny obraz")
axs[0, 1].hist(np.array(obraz).flatten(), bins=256, color="gray")
axs[0, 1].set_title("Histogram oryginalnego obrazu")

axs[1, 0].imshow(obraz5)
axs[1, 0].set_title("Obraz5")
axs[1, 1].hist(np.array(obraz5).flatten(), bins=256, color="gray")
axs[1, 1].set_title("Histogram Obraz5")

axs[2, 0].imshow(roznica, cmap="gray")
axs[2, 0].set_title("Różnica (obraz - obraz5)")
axs[2, 1].hist(roznica_np.flatten(), bins=256, color="gray")
axs[2, 1].set_title("Histogram różnicy")

plt.tight_layout()
plt.savefig('ooi5.png')



# Różnice między obraz4 i obraz5
# Wczytanie obrazów w szarości żeby łatwiej było widać różnice
obraz4 = Image.open("obraz4.jpg").convert('L')
obraz5 = obraz5.convert('L')

# Obliczenie różnicy
roznica_4_5 = ImageChops.difference(obraz4, obraz5)

# Statystyki różnicy
roznica_4_5_np = np.array(roznica_4_5)
statystyki(roznica_4_5)

fig, axs = plt.subplots(3, 2, figsize=(12, 8))
axs[0, 0].imshow(obraz4, cmap='gray')
axs[0, 0].set_title("Obraz4")
axs[0, 1].hist(np.array(obraz4).flatten(), bins=256, color="gray")
axs[0, 1].set_title("Histogram Obraz4")

axs[1, 0].imshow(obraz5, cmap='gray')
axs[1, 0].set_title("Obraz5")
axs[1, 1].hist(np.array(obraz5).flatten(), bins=256, color="gray")
axs[1, 1].set_title("Histogram Obraz5")

axs[2, 0].imshow(roznica_4_5, cmap='gray')
axs[2, 0].set_title("Różnica (obraz4 - obraz5)")
axs[2, 1].hist(roznica_4_5_np.flatten(), bins=256, color="gray")
axs[2, 1].set_title("Histogram różnicy (obraz4 - obraz5)")

plt.tight_layout()
plt.savefig('o4i5.png')

# Jak widać różnice między obrazem 4 i obrazem 5 są subtelniejsze niż różnice między oryginałem i obrazem 5 przez powtarzaną kompresję gdybym dał różnice obrazu 4 i 5 w kolorze byłyby wtedy niewidoczne

# 3



def odkoduj(obraz1, obraz2):
    tab_obraz1 = np.array(obraz1)
    tab_obraz2 = np.array(obraz2)

    roznice = np.where(tab_obraz1 != tab_obraz2, 255, 0).astype(np.uint8)

    return Image.fromarray(roznice)

jesien = Image.open("jesien.jpg")
zakodowany1 = Image.open("zakodowany2.bmp")

odkod = odkoduj(jesien, zakodowany1)
odkod.save("kod2.bmp")
