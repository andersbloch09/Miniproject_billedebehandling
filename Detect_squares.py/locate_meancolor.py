import numpy as np 
import cv2 as cv 

img = cv.imread("King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)

mean_array = np.zeros((5, 5, 3), dtype='uint8')

board_size = 5

def mean_cal(): 
    
    for j in range(board_size):
        for i in range(board_size):
            print(i,j)
         
    
    start_x = 0
    end_x = 0
    start_y = 0
    end_y = 0
    for j in range(start_y*100, end_y*100):
        for i in range(start_x*100, end_x*100):
            b = img[i,j,0]
            g = img[i,j,1]
            r = img[i,j,2]
            b_mean = b.mean
            g_mean = g.mean 
            r_mean = r.mean              
                
                
            
    return(mean_array)
        

mean_board = mean_cal()

cv.imshow("mean_board", mean_board)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()







