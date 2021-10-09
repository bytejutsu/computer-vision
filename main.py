import cv2
import numpy as np
import matplotlib.pyplot as plt


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


reeses = cv2.imread('DATA/reeses_puffs.png', 0)
cereals = cv2.imread('DATA/many_cereals.jpg', 0)


sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(reeses, None, )
kp2, des2 = sift.detectAndCompute(cereals, None, )

bf = cv2.BFMatcher()

good = []

matches = bf.knnMatch(des1, des2, k=2)

for match1, match2 in matches:
    if match1.distance < 0.75*match2.distance:
        good.append([match1])

# matches = sorted(matches, key=lambda x: x.distance)
sift_matches = cv2.drawMatchesKnn(reeses, kp1, cereals, kp2, good, None, flags=2)

display(sift_matches)
