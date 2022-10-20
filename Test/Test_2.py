#Trying median first
from venv import create
import cv2 as cv
import numpy as np

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
board_4_resize_small = cv.resize(board_4, [50, 50], interpolation = cv.INTER_AREA)
board_4_resize_large = cv.resize(board_4_resize_small, [500, 500], interpolation = cv.INTER_AREA)
board_4_median1 = cv.medianBlur(board_4_resize_small, 1)
board_4_resize_gaus = cv.resize(board_4_median1, [500, 500], interpolation = cv.INTER_AREA)
board_4_median2 = cv.medianBlur(board_4_median1, 3)
board_4_resize_median = cv.resize(board_4_median2, [500, 500], interpolation = cv.INTER_AREA)

cv.imshow("untouched", board_4)
cv.imshow("gaus", board_4_resize_gaus)
cv.imshow("median", board_4_resize_median)
cv.waitKey(0)
