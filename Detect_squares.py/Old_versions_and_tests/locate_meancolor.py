import numpy as np 
import cv2 as cv
import statistics as sta

img = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)
board_size = 5

def mean_cal():
    mean_array = np.zeros((5, 5, 3), dtype='uint8')
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

def find_landscape():
    corn = 1
    ocean = 2
    meadow = 3
    forrest = 4
    digging = 5
    swamp = 6
    not_figured = 7 
    castle = 8
    th_corn = [(0,31),(110,178),(130,220)]
    th_ocean = [(90,210),(46,150),(0,70)]
    th_meadow = [(7,51),(80,160),(55,145)]
    th_forrest = [(7,100),(34,80),(28,80)]
    th_mine = [(30,47),(53,76),(60,92)]
    th_swamp = [(41,95),(70,127),(84,133)]
    landscape_map = np.zeros((5, 5),dtype="U")
    area_map = np.zeros((5, 5),dtype="uint8")
    for j in range(board_size):
        for i in range(board_size):
            b,g,r = mean_board[i,j]
            print(i,j)
            print(mean_board[i,j])
            if b >= th_corn[0][0] and b <= th_corn[0][1] and g >= th_corn[1][0] and g <= th_corn[1][1] and r >= th_corn[2][0] and r <= th_corn[2][1]:
                if r - g > 30: 
                    landscape_map[i,j] = "not figured"
                    area_map[i,j] = not_figured
                else: 
                    landscape_map[i,j] = "corn"
                    area_map[i,j] = corn
            elif b >= th_ocean[0][0] and b <= th_ocean[0][1] and g >= th_ocean[1][0] and g <= th_ocean[1][1] and r >= th_ocean[2][0] and r <= th_ocean[2][1]:
                landscape_map[i,j] = "ocean"
                area_map[i,j] = ocean
            elif b >= th_meadow[0][0] and b <= th_meadow[0][1] and g >= th_meadow[1][0] and g <= th_meadow[1][1] and r >= th_meadow[2][0] and r <= th_meadow[2][1]:
                if g < r: 
                    if r - g > 30: 
                        landscape_map[i,j] = "not figured"
                        area_map[i,j] = not_figured
                    else:
                        landscape_map[i,j] = "swamp"
                        area_map[i,j] = swamp
                else: 
                    landscape_map[i,j] = "meadow"
                    area_map[i,j] = meadow
            elif b >= th_mine[0][0] and b <= th_mine[0][1] and g >= th_mine[1][0] and g <= th_mine[1][1] and r >= th_mine[2][0] and r <= th_mine[2][1]:
                if g - b > 35: 
                    if r < 84:
                        landscape_map[i,j] = "forrest"
                        area_map[i,j] = forrest
                    else:
                        landscape_map[i,j] = "swamp"
                        area_map[i,j] = swamp
                else:
                    landscape_map[i,j] = "digging"
                    area_map[i,j] = digging
            elif b >= th_forrest[0][0] and b <= th_forrest[0][1] and g >= th_forrest[1][0] and g <= th_forrest[1][1] and r >= th_forrest[2][0] and r <= th_forrest[2][1]:
                if r > 5+g: 
                    landscape_map[i,j] = "digging"
                    area_map[i,j] = digging
                else:
                    landscape_map[i,j] = "forrest"
                    area_map[i,j] = forrest
            elif b >= th_swamp[0][0] and b <= th_swamp[0][1] and g >= th_swamp[1][0] and g <= th_swamp[1][1] and r >= th_swamp[2][0] and r <= th_swamp[2][1]:
                landscape_map[i,j] = "swamp"
                area_map[i,j] = swamp
            else:
                landscape_map[i,j] = "not figured"
                area_map[i,j] = not_figured
    return(area_map, landscape_map)

area_layout, landscape_map = find_landscape()
print(landscape_map)
print(area_layout)

def locate_connections():
    object_array = np.zeros((5, 5), dtype="uint8")
    input_crown = area_layout[0,1] 
    print("input_crown = ", input_crown)
    a = 0
    for i in range(board_size):
        for j in range(board_size):
            if area_layout[i,j] == input_crown:
                object_array[i,j] = a 
                if object_array[i,j-1] != 0 or object_array[i-1,j] != 0:
                    if object_array[i,j-1] != 0:
                        object_array[i,j] = object_array[i,j-1]
                    if object_array[i-1,j] != 0:
                        object_array[i,j] = object_array[i-1,j]
                        if object_array[i-1,j] == a-1:
                            for k in range(board_size):
                                for l in range(board_size):
                                    if object_array[k,l] == a: 
                                        object_array[k,l] = a-1 
                            a -= 1
                                    
                else:
                    a += 1
                    object_array[i,j] = a 
            else: 
                pass


    return(object_array)     


locate_connections()


mean_resized = cv.resize(mean_board, [500,500], interpolation = cv.INTER_AREA)

cv.imshow("mean resized", mean_resized)
cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()

