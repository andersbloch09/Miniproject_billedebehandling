import numpy as np 
import cv2 as cv
import statistics as sta

img = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)

mean_array = np.zeros((5, 5, 3), dtype='uint8')
board_size = 5

def mean_cal():
    for j in range(board_size):
        for i in range(board_size):
            b_mean = []
            g_mean = []
            r_mean = []
            for y in range(j*100, 100+j*100):
                for x in range(i*100, 100+i*100): 
                   print(x,y) 
                   b = img[x,y,0]
                   g = img[x,y,1]
                   r = img[x,y,2]
                   b_mean.append(b)
                   g_mean.append(g)
                   r_mean.append(r)
            b_mean = sta.mean(b_mean)
            g_mean = sta.mean(g_mean)
            r_mean = sta.mean(r_mean)
            mean_array[i,j] = (b_mean, g_mean, r_mean)

    return(mean_array)

mean_board = mean_cal()
mean_resized = cv.resize(mean_board, [500,500], interpolation = cv.INTER_AREA)

cv.imshow("mean_resized", mean_resized)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()
