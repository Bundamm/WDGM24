from PIL import Image, ImageChops
import numpy as np

# Otwórz obraz w trybie RGB
obraz1 = Image.open("olsztyn.jpg").convert("RGB")

# Konwersja obrazu1 na tryb YCbCr
obraz2 = obraz1.convert("YCbCr")

# Zapisz obraz2
obraz2.save("obraz2.jpg")

# Pokaż obraz2
obraz2.show()


# Funkcja do konwersji kanałów RGB na YCbCr
def rgb_to_ycbcr(image):
    # Konwertujemy obraz do tablicy NumPy w trybie RGB
    img_array = np.array(image)

    # Wyodrębnianie kanałów R, G, B
    R = img_array[:, :, 0]
    G = img_array[:, :, 1]
    B = img_array[:, :, 2]

    # Wyznaczanie kanałów Y, Cb, Cr zgodnie z formułami
    Y = 16. + (64.738 * R + 129.057 * G + 25.064 * B) / 255.
    Cb = 128. + (-37.945 * R - 74.494 * G + 112.439 * B) / 255.
    Cr = 128. + (112.439 * R - 94.154 * G - 18.285 * B) / 255.

    # Łączenie kanałów Y, Cb, Cr w jeden obraz
    ycbcr_image = np.stack((Y, Cb, Cr), axis=-1)

    # Zwracamy wynik jako obraz Pillow w trybie YCbCr
    return Image.fromarray(np.uint8(ycbcr_image))


# Zastosowanie funkcji do obrazu1
obraz3 = rgb_to_ycbcr(obraz1)

# Zapisz obraz3
obraz3.save("obraz3.jpg")

# Pokaż obraz3
obraz3.show()

# Otwórz obraz2 i obraz3
obraz2 = Image.open("obraz2.jpg")
obraz3 = Image.open("obraz3.jpg")

# Porównanie obrazów
difference = ImageChops.difference(obraz2, obraz3)

# Jeśli różnica to czarny obraz, oznacza to, że obrazy są identyczne
difference.show()

# Możesz zapisać różnicę, aby sprawdzić, czy istnieje jakakolwiek różnica
difference.save("difference.jpg")

# Przekonwertowanie obraz2 (YCbCr) na RGB
obraz4 = obraz2.convert("RGB")

# Zapisz obraz4
obraz4.save("obraz4.jpg")

# Pokaż obraz4
obraz4.show()

# Porównanie obraz1 i obraz4
difference = ImageChops.difference(obraz1, obraz4)
difference.show()

# Zapisz różnicę, aby zobaczyć, czy obrazy są identyczne
difference.save("difference_rgb.jpg")