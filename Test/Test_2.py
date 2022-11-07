import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


board = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\7.jpg", 1)
board_gray = cv.cvtColor(board, cv.COLOR_BGR2GRAY)
template = cv.imread(r'Crown_full.png',0)
template = cv.resize(template, [33,25], interpolation = cv.INTER_AREA)


w, h = template.shape[::-1]
res = cv.matchTemplate(board_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.80
loc = np.where (res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(board, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',board)
cv.imshow("untouched", board)
cv.imshow("gray", board_gray)
cv.imshow("gray_template", template)
cv.waitKey(0)