from PIL import Image
import numpy as np

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
