from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

#1
im = Image.open('melon.png')
print(im.mode)
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
plt.show()

