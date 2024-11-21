from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randrange

# m310 = Image.open('mix310.png')
# r,g,b = m310.split()
# m311 = Image.merge('RGB', (g,r,b))
# m311.show()

# def szary(w,h):
#     array = np.zeros((h,w), dtype=int)
#
#     for i in range(h):
#         for j in range(w):
#             array[i,j] = (3*i+j) % 256
#     image = Image.fromarray(array.astype('uint8'), mode='L')
#     return image
#
# o10 = Image.open('obraz10.jpg')
# w, h = o10.size
# szar = szary(w, h)
# r,g,b = o10.split()
# mix = Image.merge('RGB', (szar, g, b))
# mix.show()
# mix.save('mix.png')

o10 = Image.open('obraz10.jpg')
s = stat.Stat(o10)
print("Odchylenie standardowe: ", s.stddev)
#[65.0,40.1,42.4]

