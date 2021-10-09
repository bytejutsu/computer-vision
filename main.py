import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('DATA/sammy_face.jpg')

blurred_img = cv2.blur(img, ksize=(5, 5))

# med_val = np.median(img)
med_val = np.median(blurred_img)

lower = int(max(0, 0.7*med_val))
upper = int(min(255, 1.3*med_val)) + 50

edges = cv2.Canny(image=blurred_img, threshold1=lower, threshold2=upper)

plt.imshow(edges)
plt.show()
