import cv2 as cv
import numpy as np
import math

img = cv.imread("mean_board_25.png",1)

cv.imshow("mean_board_25", img)
board_size = 5 

for j in range(board_size):
    for i in range(board_size):
        print(img[i,j])

meadow  = 24 142 83
not_figured =  30 102 135

d = math.sqrt((img[i,j,0]-img[i,j,0])^2)
print(d)




cv.waitKey(0)
cv.destroyAllWindows()