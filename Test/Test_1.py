import numpy as np 
import cv2 as cv
import statistics as sta
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

board = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
threshold = 0.80

templateup = cv.imread(r'Crown_full.png',1)
templateup = cv.resize(templateup, [30,22], interpolation = cv.INTER_AREA)
(y,x,channels) = templateup.shape[::]
res = cv.matchTemplate(board,templateup,cv.TM_CCOEFF_NORMED)

loc = np.where (res >= threshold)
for pt in zip(*loc[::]):
    cv.rectangle(board, pt, (pt[0] + x, pt[1] + y), (0,255,0), 1)

cv.imwrite('res.png',board)
cv.imshow("untouched", board)
cv.imshow("gray_template", templateup)
cv.waitKey(0)