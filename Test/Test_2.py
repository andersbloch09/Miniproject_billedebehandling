import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


board = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\9.jpg", 1)
board_gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
threshold = 0.60


templateup = cv.imread(r'Crown_full.png',1)
templateup = cv.resize(templateup, [30,22], interpolation = cv.INTER_AREA)
w, h, g = templateup.shape[::-1]
res = cv.matchTemplate(board,templateup,cv.TM_CCOEFF_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)

templateleft = cv.imread(r'crown cropped 4 left.png',1)
templateleft = cv.resize(templateleft, [22,30], interpolation = cv.INTER_AREA)
w, h, g  = templateup.shape[::-1]
res = cv.matchTemplate(board,templateup,cv.TM_CCOEFF_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

templatedown = cv.imread(r'crown cropped 4 down.png',1)
templatedown = cv.resize(templatedown, [30,22], interpolation = cv.INTER_AREA)
w, h, g = templateup.shape[::-1]
res = cv.matchTemplate(board,templateup,cv.TM_CCOEFF_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

templateright = cv.imread(r'crown cropped 4 right.png',1)
templateright = cv.resize(templateright, [22,30], interpolation = cv.INTER_AREA)
w, h, g = templateup.shape[::-1]
res = cv.matchTemplate(board,templateup,cv.TM_CCOEFF_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (255,0,255), 2)

cv.imshow('left', templateleft)
cv.imwrite('res.png',board)
cv.imshow("untouched", board)
cv.imshow("gray", board_gray)
cv.imshow("gray_template", templateup)
cv.waitKey(0)