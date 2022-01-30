import cv2
import numpy as np

window = "Drawing"
# Create black empty images
W = 1000
size = W, W, 3
drawing = np.zeros(size, dtype=np.uint8)


SQUARE_SZ, DIST = 100, 10
color = (255, 255, 255)

y = DIST
for x in range(DIST, W, SQUARE_SZ+DIST):
    for y in range(DIST, W, SQUARE_SZ+DIST):
        cv2.rectangle(drawing, (x, y), (x+SQUARE_SZ, y+SQUARE_SZ), color, -1)


cv2.imshow(window, drawing)
cv2.waitKey(0)
