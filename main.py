import cv2
import time
import numpy as np

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

full = cv2.imread('DATA/sammy.jpg')

full_copy = full.copy()

face = cv2.imread('DATA/sammy_face.jpg')

method = eval('cv2.TM_CCOEFF')

res = cv2.matchTemplate(full, face, method)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

if method in [cv2.TM_SQDIFF, cv2.TM_CCORR_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

height, width, channels = face.shape

bottom_right = (top_left[0]+width, top_left[1]+height)

cv2.rectangle(full_copy, top_left, bottom_right, (255, 0, 0), 10)

cv2.namedWindow('Window')

while True:

    cv2.imshow('Window', full_copy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
