import cv2
import numpy as np


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(fixed_dog_backpack, (x, y), 60, (0, 0, 255), 10)


##############################################

cv2.namedWindow('my_drawing', cv2.WINDOW_GUI_NORMAL)

cv2.setMouseCallback('my_drawing', draw_circle)

##############################################

fixed_dog_backpack = cv2.imread('DATA/dog_backpack.jpg')

# fixed_dog_backpack = cv2.cvtColor(dog_backpack, cv2.COLOR_BGR2RGB)

cv2.rectangle(fixed_dog_backpack, (300, 300), (550, 550), (0, 0, 255), 5)

while True:

    cv2.imshow('my_drawing', fixed_dog_backpack)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
