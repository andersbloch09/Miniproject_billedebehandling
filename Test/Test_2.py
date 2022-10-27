#Trying median first
from venv import create
import cv2 as cv
import numpy as np

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
(y, x, channels) = board_4.shape
for i in range(0, y, 1):
    for j in range(0, x, 1):
        


cv.imshow("untouched", board_4)
cv.waitKey(0)
