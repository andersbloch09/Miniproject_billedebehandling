#Hallo dette er test 1 til github
#dette er andet push
#så piller jeg heller ikke ved dit
from venv import create
import cv2 as cv
import numpy as np

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
board_4_resize_small = cv.resize(board_4, [75, 75], interpolation = cv.INTER_AREA)
board_4_resize_large = cv.resize(board_4_resize_small, [500, 500], interpolation = cv.INTER_AREA)
board_4_gaus = cv.GaussianBlur(board_4_resize_large, (13,13), 1)
board_4_resize_gaus = cv.resize(board_4_gaus, [500, 500], interpolation = cv.INTER_AREA) 
board_4_median = cv.medianBlur(board_4_resize_large, 9)
board_4_resize_small_2 = cv.resize(board_4_median, [75, 75], interpolation = cv.INTER_AREA)
board_4_gaus_2 = cv.GaussianBlur(board_4_resize_small_2, (3,3), 0)
board_4_resize_gaus_2 = cv.resize(board_4_gaus_2, [500, 500], interpolation = cv.INTER_AREA)
board_4_median_2 = cv.medianBlur(board_4_resize_gaus_2, 15)

cv.imshow("untouched", board_4)
cv.imshow("gaus", board_4_resize_gaus)
cv.imshow("gaus2", board_4_resize_gaus_2)
cv.imshow("median", board_4_median)
cv.imshow("median2", board_4_median_2)
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
        