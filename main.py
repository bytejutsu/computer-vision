import cv2
import time
import numpy as np

# # GLOBAL VARIABLES

pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False

# # CALLBACK FUNCTION RECTANGLE


def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # RESET THE RECTANGLE (IT CHECKS IF THE RECT IS THERE)
        if topLeft_clicked and botRight_clicked:
            topLeft_clicked = False
            botRight_clicked = False
            pt1 = (0, 0)
            pt2 = (0, 0)

        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True

        elif not botRight_clicked:
            pt2 = (x, y)
            botRight_clicked = True


# # CONNECT TO THE CALLBACK

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TOP LEFT CORNER

x = width // 2
y = height // 2

# width and height of RECTANGLE

w = width // 4
h = height // 4

# BOTTOM RIGHT x + w , y + h

while True:

    ret, frame = cap.read()

    # DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
