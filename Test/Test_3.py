import cv2 as cv
import numpy as np 

board = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\15.jpg",1)
board_resize_small = cv.resize(board, [40,40], interpolation = cv.INTER_AREA)

(y,x,channels) = board.shape

print(y,x,channels)

def threshold_ocean():
    threshold = [(120,220),(0,90),(0,50)]
    output_image_o = np.zeros(board.shape, dtype=board.dtype)
    b,g,r = 0,0,0
    for j in range(y):
        for i in range(x):
            b,g,r = board[i,j]
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
            output_image_o[i,j] = (pixelvalB, pixelvalG, pixelvalR)
    threshold_o = output_image_o 
    b = threshold_o[:,:,0]
    g = threshold_o[:,:,1]
    r = threshold_o[:,:,2]
    threshold_ocean_gray = (b//3)+(g//3)+(r//3) 
    kernel = np.ones((29,29), np.uint8)  
    dila_ocean = cv.dilate(threshold_ocean_gray, kernel, iterations=1)  
    return(dila_ocean)          

def threshold_meadow():
    threshold = [(30,40),(135,155),(79,99)]
    output_image_m = np.zeros(board.shape, dtype=board.dtype)
    b,g,r = 0,0,0
    for j in range(y):
        for i in range(x):
            b,g,r = board[i,j]
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
            output_image_m[i,j] = (pixelvalB, pixelvalG, pixelvalR)
    threshold_o = output_image_m 
    b = threshold_o[:,:,0]
    g = threshold_o[:,:,1]
    r = threshold_o[:,:,2]
    threshold_ocean_gray = (b//3)+(g//3)+(r//3) 
    kernel = np.ones((29,29), np.uint8)  
    dila_meadow = cv.dilate(threshold_ocean_gray, kernel, iterations=1)  
    return(dila_meadow)                  

def threshold_corn():
    threshold = [(0,15),(130,160),(175,205)]
    output_image_c = np.zeros(board.shape, dtype=board.dtype)
    b,g,r = 0,0,0
    for j in range(y):
        for i in range(x):
            b,g,r = board[i,j]
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
            output_image_c[i,j] = (pixelvalB, pixelvalG, pixelvalR)          
    threshold_o = output_image_c
    b = threshold_o[:,:,0]
    g = threshold_o[:,:,1]
    r = threshold_o[:,:,2]
    threshold_ocean_gray = (b//3)+(g//3)+(r//3) 
    kernel = np.ones((29,29), np.uint8)  
    dila_corn = cv.dilate(threshold_ocean_gray, kernel, iterations=1)  
    return(dila_corn)          

def threshold_forrest():
    threshold = [(17,17),(0,15),(35,40)]
    output_image_f = np.zeros(board.shape, dtype=board.dtype)
    b,g,r = 0,0,0
    for j in range(y):
        for i in range(x):
            b,g,r = board[i,j]
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
            output_image_f[i,j] = (pixelvalB, pixelvalG, pixelvalR)          
    threshold_o = output_image_f 
    b = threshold_o[:,:,0]
    g = threshold_o[:,:,1]
    r = threshold_o[:,:,2]
    dila_forrest = (b//3)+(g//3)+(r//3) 
    kernel_d = np.ones((7,7), np.uint8)
    kernel_d_2 = np.ones((59,59), np.uint8)
    kernel_e = np.ones((13,13), np.uint8)
    dila_forrest = cv.dilate(dila_forrest, kernel_d, iterations=1)
    dila_forrest = cv.erode(dila_forrest, kernel_e, iterations=1)  
    dila_forrest = cv.dilate(dila_forrest, kernel_d_2, iterations=1)
       
    return(dila_forrest)           

# def grayscale():
#     b = threshold_o[:,:,0]
#     g = threshold_o[:,:,1]
#     r = threshold_o[:,:,2]

#     threshold_ocean_gray = (b//3)+(g//3)+(r//3)    
    
#     return(threshold_ocean_gray)

# kernel = np.ones((29,29), np.uint8)  
# dila_ocean = cv.dilate(threshold_ocean_gray, kernel, iterations=1)  
dila_ocean = threshold_ocean()
dila_meadow = threshold_meadow()
dila_corn = threshold_corn()
dila_forrest = threshold_forrest()
cv.imshow("Board 4", board)
cv.imshow("Tresh_dila_ocean", dila_ocean)
cv.imshow("Tresh_dila_meadow", dila_meadow)
cv.imshow("Tresh_dila_corn", dila_corn)
cv.imshow("Tresh_dila_forrest", dila_forrest)
cv.waitKey()
cv.destroyAllWindows()





