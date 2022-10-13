#Hallo dette er test 1 til github
#dette er andet push
#så piller jeg heller ikke ved dit
from venv import create
import cv2 as cv
import numpy as np

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
board_4_resize_small = cv.resize(board_4, [50, 50], interpolation = cv.INTER_AREA)
board_4_resize_large = cv.resize(board_4_resize_small, [500, 500], interpolation = cv.INTER_AREA)
board_4_gaus = cv.GaussianBlur(board_4_resize_large, (51,51), 0)
board_4_median = cv.medianBlur(board_4_gaus, 51)
board_4_resize_median = cv.resize(board_4_median, [500, 500], interpolation = cv.INTER_AREA)
board_4_resize_gaus = cv.resize(board_4_gaus, [500, 500], interpolation = cv.INTER_AREA)
cv.imshow("untouched", board_4)
cv.imshow("gaus", board_4_resize_gaus)
cv.imshow("median", board_4_resize_median)
cv.waitKey(0)

(y, x, channels) = board_4.shape
print(y, x, channels)
i=0
j=0
mean_radius = 1

def create_meanfilter():
    ones_imput = (2*mean_radius) + 1
    mean_filter = np.ones((ones_imput, ones_imput), dtype='uint8')
    print(mean_filter)


#  for i in range (0, y, 1):
#     for j in range (0, x, 1):
#         b,g,r = board_4[i,j]
#         print(b,g,r)
#         pass
        