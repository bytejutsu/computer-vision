import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.int16)

print(blank_img.shape)

# cv2.rectangle(blank_img, pt1=(225, 225), pt2=(300, 300), color=(0, 255, 0), thickness=10)

# cv2.circle(img=blank_img, center=(256, 256), radius=50, color=(255, 0, 0), thickness=8)

# cv2.line(blank_img, pt1=(0, 0), pt2=(512, 512), color=(102, 255, 255), thickness=5)

# font = cv2.FONT_HERSHEY_SIMPLEX

# cv2.putText(blank_img, text="Hello", org=(10, 500), fontFace=font, fontScale=4, color=(255, 255, 255), thickness=3, lineType=cv2.LINE_AA)

vertices = np.array([[100, 300], [200, 200], [400, 300], [200, 400]])

vertices.shape

pts = vertices.reshape((-1, 1, 2))

cv2.polylines(blank_img, [pts], isClosed=True, color=(255, 0, 0), thickness=5)



plt.imshow(blank_img, cmap='gray')
plt.show()
