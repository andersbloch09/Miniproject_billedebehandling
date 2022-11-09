import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


board = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/9.jpg", 1)
board_gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
threshold = 0.96


templateup = cv.imread(r'Test_pictures/Crown_full.png',0)
templateup = cv.resize(templateup, [30,22], interpolation = cv.INTER_AREA)
w, h = templateup.shape[::-1]
res = cv.matchTemplate(board_gray,templateup,cv.TM_CCORR_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

cv.imshow("untouched", board)
cv.imshow("gray", board_gray)
cv.imshow("gray_template", templateup)
cv.waitKey(0)