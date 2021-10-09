import cv2
import time
import numpy as np

real_chess = cv2.imread('DATA/real_chessboard.jpg')
real_chess_gray = cv2.cvtColor(real_chess, cv2.COLOR_RGB2GRAY)

flat_chess = cv2.imread('DATA/flat_chessboard.png')
flat_chess_gray = cv2.cvtColor(flat_chess, cv2.COLOR_RGB2GRAY)

corners = cv2.goodFeaturesToTrack(real_chess_gray, 1000, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(real_chess, (x, y), 3, (255, 0, 0), -1)

cv2.namedWindow('Window')

while True:

    cv2.imshow('Window', real_chess)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
