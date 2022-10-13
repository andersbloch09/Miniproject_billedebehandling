import cv2 as cv
import numpy as np 

board_4 = cv.imread("King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)
board_4_resize_small = cv.resize(board_4, [40,40], interpolation = cv.INTER_AREA)
board_4_resize_large = cv.resize(board_4_resize_small, [1500,1500], interpolation = cv.INTER_AREA)

(y,x,channels) = board_4_resize_small.shape

print(y,x,channels)


cv.imshow("Board 4", board_4_resize_large)
cv.waitKey()
cv.destroyAllWindows()

