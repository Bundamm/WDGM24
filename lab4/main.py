from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randrange

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