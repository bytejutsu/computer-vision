import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

dots = cv2.imread('DATA/dot_grid.png')

found, corners = cv2.findCirclesGrid(dots, (10, 10), cv2.CALIB_CB_SYMMETRIC_GRID)

print(found)

cv2.drawChessboardCorners(dots, (10, 10), corners, found)

plt.imshow(dots)
plt.show()
