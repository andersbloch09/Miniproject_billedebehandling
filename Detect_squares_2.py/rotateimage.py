import cv2 as cv 
import numpy

img = cv.imread("Detect_squares_2.py/Assests/crown_swamp.png",0)


for i in range(4):
    if i > 0: 
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        cv.imwrite("rotated_template"+ str(i) +".png",img)


