from PIL import Image
import numpy as np
from PIL import ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

#1
im = Image.open("zeby.png").convert('L')


# Funkcja do obliczania histogramu znormalizowanego
def histogram_norm(image):
    hist = np.histogram(image, bins=256, range=(0, 256))[0]
    return hist / hist.sum()

# Funkcja do obliczania histogramu skumulowanego
def histogram_cumul(image):
    hist_norm = histogram_norm(image)
    return np.cumsum(hist_norm)

# Funkcja do wyrównania histogramu
def histogram_equalization(image):
    hist_cumul = histogram_cumul(image)
    equalized_array = np.floor(255 * hist_cumul[image]).astype('uint8')
    return Image.fromarray(equalized_array)

# Funkcja do konwersji obrazu RGB na L z wagami
def konwertuj1(image, w_r, w_g, w_b):
    array = np.array(image)
    L = np.round(array[:, :, 0] * w_r + array[:, :, 1] * w_g + array[:, :, 2] * w_b).astype('uint8')
    return Image.fromarray(L, mode='L')

def konwertuj2(image, w_r, w_g, w_b):
    array = np.array(image)
    L = np.int_((array[:, :, 0] * w_r + array[:, :, 1] * w_g + array[:, :, 2] * w_b)).astype('uint8')
    return Image.fromarray(L, mode='L')

def image_stats(im):
    s = stat.Stat(im)
    print("mean ", s.mean)
    print("stddev ", s.stddev)

# Zadanie 2.1-2.3: Obliczanie histogramów i wyrównanie histogramu
hist_norm = histogram_norm(im)
hist_cumul = histogram_cumul(im)
obraz_equalized = histogram_equalization(np.array(im))
obraz_equalized.save("equalized.png")

image_stats(obraz_equalized)
image_stats(im)


# Rysowanie histogramów
plt.figure()
plt.title("Histogramy")
plt.hist(np.array(im).flatten(), bins=256, alpha=0.5, label="Oryginalny")
plt.plot(hist_norm, label="Znormalizowany")
plt.plot(hist_cumul * 255, label="Skumulowany")
plt.hist(np.array(obraz_equalized).flatten(), bins=256, alpha=0.5, label="Wyrównany")
plt.legend()

plt.savefig("fig1.png")
plt.show()

# Zadanie 3: Wyrównanie za pomocą ImageOps.equalize
obraz_equalized1 = ImageOps.equalize(im)
obraz_equalized1.save("equalized1.png")

# Rysowanie porównania obrazów
plt.figure()
plt.title("Porównanie obrazów")
plt.subplot(1, 3, 1)
plt.imshow(im, cmap='gray')
plt.title("Oryginalny")
plt.subplot(1, 3, 2)
plt.imshow(obraz_equalized, cmap='gray')
plt.title("Equalized")
plt.subplot(1, 3, 3)
plt.imshow(obraz_equalized1, cmap='gray')
plt.title("ImageOps Equalized")
plt.savefig("fig2.png")

# Zadanie 4: Konwersja RGB na L
mgla = Image.open("mgla.jpg")
mgla_L1 = konwertuj1(mgla, 0.299, 0.587, 0.114)
mgla_L1.save("mgla_L1.png")
mgla_L = mgla.convert('L')
mgla_L.save("mgla_L.png")
mgla_L2 = konwertuj2(mgla, 0.299, 0.587, 0.114)
mgla_L2.save("mgla_L2.png")

# Statystyki obrazów
print("Statystyki obrazów:")
print("mgla_L:")
image_stats(mgla_L)
print("mgla_L1:")
image_stats(mgla_L1)
print("mgla_L2:")
image_stats(mgla_L2)

