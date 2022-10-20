import timeit
import cv2 as cv
import numpy as np 

board_4 = cv.imread("King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)
board_4_resize_small = cv.resize(board_4, [40,40], interpolation = cv.INTER_AREA)

(y,x,channels) = board_4.shape

print(y,x,channels)

#board_4 = cv.medianBlur(board_4, 5)

def threshold_b():
    threshold = [(120,220),(0,90),(0,50)]
    output_image = np.zeros(board_4.shape, dtype=board_4.dtype)
    b,g,r = 0,0,0
    for j in range(y):
        for i in range(x):
            b,g,r = board_4[i,j]
            if b <= threshold[0][0] or b >= threshold[0][1] and g <= threshold[1][0] or g >= threshold[1][1] and r <= threshold[2][0] or r >= threshold[2][1]:
                b = 0
                g = 0
                r = 0
            else: 
                b = 255
                g = 255
                r = 255
            pixelvalB = b
            pixelvalG = g
            pixelvalR = r
            output_image[i,j] = (pixelvalB, pixelvalG, pixelvalR)
            
    return(output_image)          

thresholded_b = threshold_b()

cv.imwrite("Thresholded_b.png", thresholded_b)

board_4_gray = cv.imread("Thresholded_b.png",0)

kernel = np.ones((29,29), np.uint8)  
dila_ocean = cv.dilate(board_4_gray, kernel, iterations=1)  

thresholded_b = threshold_b()

cv.imshow("Board 4", board_4)
cv.imshow("Thresholded for blue", thresholded_b)
cv.imshow("Dilation_b", dila_ocean)
cv.waitKey()
cv.destroyAllWindows()


