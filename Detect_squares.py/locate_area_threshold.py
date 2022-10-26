import cv2 as cv
import numpy as np 

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg",1)
board_4_resize_small = cv.resize(board_4, [40,40], interpolation = cv.INTER_AREA)
(y,x,channels) = board_4.shape
print(y,x,channels)

def threshold_ocean():
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
    b = output_image[:,:,0]
    g = output_image[:,:,1]
    r = output_image[:,:,2]

    output_image = (b//3)+(g//3)+(r//3)   
    return(output_image)          

def threshold_corn():
    threshold = [(3,10),(165,180),(185,230)]
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
    b = output_image[:,:,0]
    g = output_image[:,:,1]
    r = output_image[:,:,2]

    output_image = (b//3)+(g//3)+(r//3)   
    return(output_image)          

def threshold_meadow():
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
    b = output_image[:,:,0]
    g = output_image[:,:,1]
    r = output_image[:,:,2]

    output_image = (b//3)+(g//3)+(r//3)   
    return(output_image)          

def threshold_forrest():
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
    b = output_image[:,:,0]
    g = output_image[:,:,1]
    r = output_image[:,:,2]

    output_image = (b//3)+(g//3)+(r//3)   
    return(output_image)          

board_4__o_gray = threshold_ocean()
kernel = np.ones((21,21), np.uint8)  
dila_ocean = cv.dilate(board_4__o_gray, kernel, iterations=1)  
threshold_o = threshold_ocean()

board_4__c_gray = threshold_corn() 
kernel = np.ones((3,3), np.uint8) 
ero_corn = cv.erode(board_4__c_gray, kernel, iterations=1) 
kernel = np.ones((9,9), np.uint8)
dila_corn = cv.dilate(ero_corn, kernel, iterations=1)
threshold_c = threshold_corn()

board_4__m_gray = threshold_meadow()
kernel = np.ones((21,21), np.uint8)  
dila_meadow = cv.dilate(board_4__m_gray, kernel, iterations=1)  
threshold_m = threshold_meadow()

board_4__f_gray = threshold_forrest()
kernel = np.ones((21,21), np.uint8)  
dila_forrest = cv.dilate(board_4__f_gray, kernel, iterations=1)  
threshold_f = threshold_ocean()


cv.imshow("Board 4", board_4)
cv.imshow("Thresholded for ocean", threshold_o)
cv.imshow("Dilation_o", dila_ocean)
cv.imshow("Thresholded for corn", threshold_c)
cv.imshow("Dilation_c", dila_corn)
cv.waitKey()
cv.destroyAllWindows()


