import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('DATA/flat_chessboard.png')

found, corners = cv2.findChessboardCorners(flat_chess, (7, 7))

print(found)

cv2.drawChessboardCorners(flat_chess, (7, 7), corners, found)

plt.imshow(flat_chess)
plt.show()
