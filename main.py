import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mat = np.ones(shape=(5, 5)) * 10

print(mat)

np.random.seed(101)

arr = np.random.randint(low=0, high=100, size=(5, 5))

print(arr)

print(arr.max())

print(arr.min())

# R G B

# RED CHANNEL: 0 -> no red == (pure black) | 255 -> full pure red (pure white)

pic = Image.open('DATA/00-puppy.jpg')

pic_arr = np.asarray(pic)

print(pic_arr.shape)

pic_blue = pic_arr.copy()

pic_blue[:, :, 0] = 0
pic_blue[:, :, 1] = 0

plt.imshow(pic_blue)
plt.show()
