import numpy as np 
import cv2 as cv  

img = cv.imread("King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)

mean_array = np.zeros((5, 5, 3), dtype='uint8')

board_size = 5

def mean_cal():
    for j in range(board_size):
        for i in range(board_size):
            for y in range(j*100, 100+j*100):
                for x in range(i*100, 100+i*100): 
                   print(x,y)
                   b = img[i,j,0]
                   g = img[i,j,1]
                   r = img[i,j,2]
                   b = b + b.mean()
                   g = g + g.mean()
                   r = r + r.mean()
                   mean_array[i,j]=(b,g,r)

    return(mean_array)

mean_board = mean_cal()
mean_resized = cv.resize(mean_board, [500,500], interpolation = cv.INTER_AREA)

cv.imshow("mean_resized", mean_resized)
#cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()
