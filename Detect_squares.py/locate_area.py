import timeit
import cv2 as cv
import numpy as np 

board_4 = cv.imread("King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)
board_4_resize_small = cv.resize(board_4, [40,40], interpolation = cv.INTER_AREA)

(y,x,channels) = board_4_resize_small.shape

print(y,x,channels)


def threshold_rgb():
    threshold = [(30,45),(30,45),(30,45)]
    output_image = np.zeros(board_4_resize_small.shape, dtype=board_4_resize_small.dtype)
    for j in range(y):
        for i in range(x):
            b,g,r = board_4_resize_small[i,j]
            if b < threshold[0][0] or b > threshold[0][1]:
                b = 0
            else: 
                b = 255
            if g < threshold[1][0] or g > threshold[1][1]:
                g = 0
            else: 
                g = 255
            if r < threshold[2][0] or r > threshold[2][1]:
                r = 0
            else: 
                r = 255
            pixelvalB = b
            pixelvalG = g
            pixelvalR = g
            output_image[i,j] = (pixelvalB, pixelvalG, pixelvalR)
            
    return(output_image)          

thresholded_b = threshold_rgb()
board_4_resize_large = cv.resize(thresholded_b, [1500,1500], interpolation = cv.INTER_AREA)

cv.imshow("Board 4", board_4)
cv.imshow("Thresholded for blue", board_4_resize_large)
cv.waitKey()
cv.destroyAllWindows()


