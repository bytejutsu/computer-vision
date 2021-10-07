import cv2
import numpy as np

# VARIABLES

# True while mouse button down, False while mouse button UP
drawing = False
ix = -1
iy = -1


# FUNCTIONS


def draw_rectangle(event, x, y, flags, param):

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:

        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)

##############################################
cv2.namedWindow('my_drawing', cv2.WINDOW_GUI_NORMAL)

cv2.setMouseCallback('my_drawing', draw_rectangle)

##############################################

img = np.zeros((512, 512, 3), np.int8)

while True:

    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break


cv2.destroyAllWindows()
