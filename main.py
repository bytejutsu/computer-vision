import cv2
import numpy as np
import matplotlib.pyplot as plt


def display(img, cmap='gray'):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()


nadia = cv2.imread('DATA/Nadia_Murad.jpg', 0)
denis = cv2.imread('DATA/Denis_Mukwege.jpg', 0)
solvay = cv2.imread('DATA/solvay_conference.jpg', 0)

car_plates = cv2.imread('DATA/car_plate.jpg', 0)

face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_eye.xml')
car_plate_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_russian_plate_number.xml')


def detect_car_plates(img):
    car_plate_img = img.copy()

    car_plate_rects = car_plate_cascade.detectMultiScale(car_plate_img, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in car_plate_rects:
        cv2.rectangle(car_plate_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return car_plate_img


def blur_car_plates(img):
    car_plate_img = img.copy()
    roi = img.copy()

    car_plate_rects = car_plate_cascade.detectMultiScale(car_plate_img, scaleFactor=1.3, minNeighbors=3)

    for (x, y, w, h) in car_plate_rects:
        roi = roi[y:y+h, x:x+w]
        blurred_roi = cv2.medianBlur(roi, 7)
        car_plate_img[y:y+h, x:x+w] = blurred_roi

    return car_plate_img


result = blur_car_plates(car_plates)
display(result)
