import numpy as np 
import cv2 as cv
import statistics as sta



class image_handler():
    def __init__(self):
        self.img = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/4.jpg",1)
        self.board_size = 5
    
    def find_castle(self):
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        
    
    def mean_cal(self):
        self.mean_array = np.zeros((5, 5, 3), dtype='uint8')
        for j in range(self.board_size):
            for i in range(self.board_size):
                b_mean = []
                g_mean = []
                r_mean = []
                for y in range(j*100, 100+j*100):
                    for x in range(i*100, 100+i*100): 
                        print(x,y) 
                        b = self.img[x,y,0]
                        g = self.img[x,y,1]
                        r = self.img[x,y,2]
                        b_mean.append(b)
                        g_mean.append(g)
                        r_mean.append(r)
                b_mean = sta.mean(b_mean)
                g_mean = sta.mean(g_mean)
                r_mean = sta.mean(r_mean)
                self.mean_array[i,j] = (b_mean, g_mean, r_mean)


    def find_landscape(self):
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
        self.landscape_map = np.zeros((5, 5),dtype="U")
        self.area_map = np.zeros((5, 5),dtype="uint8")
        for j in range(self.board_size):
            for i in range(self.board_size):
                b,g,r = self.mean_array[i,j]
                print(i,j)
                print(self.mean_array[i,j])
                if b >= th_corn[0][0] and b <= th_corn[0][1] and g >= th_corn[1][0] and g <= th_corn[1][1] and r >= th_corn[2][0] and r <= th_corn[2][1]:
                    if r - g > 30: 
                        self.landscape_map[i,j] = "not figured"
                        self.area_map[i,j] = not_figured
                    else: 
                        self.landscape_map[i,j] = "corn"
                        self.area_map[i,j] = corn
                elif b >= th_ocean[0][0] and b <= th_ocean[0][1] and g >= th_ocean[1][0] and g <= th_ocean[1][1] and r >= th_ocean[2][0] and r <= th_ocean[2][1]:
                    self.landscape_map[i,j] = "ocean"
                    self.area_map[i,j] = ocean
                elif b >= th_meadow[0][0] and b <= th_meadow[0][1] and g >= th_meadow[1][0] and g <= th_meadow[1][1] and r >= th_meadow[2][0] and r <= th_meadow[2][1]:
                    if g < r: 
                        if r - g > 30: 
                            self.landscape_map[i,j] = "not figured"
                            self.area_map[i,j] = not_figured
                        else:
                            self.landscape_map[i,j] = "swamp"
                            self.area_map[i,j] = swamp
                    else: 
                        self.landscape_map[i,j] = "meadow"
                        self.area_map[i,j] = meadow
                elif b >= th_mine[0][0] and b <= th_mine[0][1] and g >= th_mine[1][0] and g <= th_mine[1][1] and r >= th_mine[2][0] and r <= th_mine[2][1]:
                    if g - b > 35: 
                        if r < 84:
                            self.landscape_map[i,j] = "forrest"
                            self.area_map[i,j] = forrest
                        else:
                            self.landscape_map[i,j] = "swamp"
                            self.area_map[i,j] = swamp
                    else:
                        self.landscape_map[i,j] = "digging"
                        self.area_map[i,j] = digging
                elif b >= th_forrest[0][0] and b <= th_forrest[0][1] and g >= th_forrest[1][0] and g <= th_forrest[1][1] and r >= th_forrest[2][0] and r <= th_forrest[2][1]:
                    if r > 5+g: 
                        self.landscape_map[i,j] = "digging"
                        self.area_map[i,j] = digging
                    else:
                        self.landscape_map[i,j] = "forrest"
                        self.area_map[i,j] = forrest
                elif b >= th_swamp[0][0] and b <= th_swamp[0][1] and g >= th_swamp[1][0] and g <= th_swamp[1][1] and r >= th_swamp[2][0] and r <= th_swamp[2][1]:
                    self.landscape_map[i,j] = "swamp"
                    self.area_map[i,j] = swamp
                else:
                    self.landscape_map[i,j] = "not figured"
                    self.area_map[i,j] = not_figured
        
        
    def locate_connections(self):
        self.object_array = np.zeros((5, 5), dtype="uint8")
        self.input_crown = self.area_map[0,1] 
        print("input_crown = ", self.input_crown)
        a = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.area_map[i,j] == self.input_crown:
                    self.object_array[i,j] = a 
                    if self.object_array[i,j-1] != 0 or self.object_array[i-1,j] != 0:
                        if self.object_array[i,j-1] != 0:
                            self.object_array[i,j] = self.object_array[i,j-1]
                        if self.object_array[i-1,j] != 0:
                            self.object_array[i,j] = self.object_array[i-1,j]
                            if self.object_array[i-1,j] == a-1:
                                for k in range(self.board_size):
                                    for l in range(self.board_size):
                                        if self.object_array[k,l] == a: 
                                            self.object_array[k,l] = a-1 
                                a -= 1
                                        
                    else:
                        a += 1
                        self.object_array[i,j] = a 
                else: 
                    pass


pic = image_handler()
pic.mean_cal()
pic.find_landscape()
pic.locate_connections()

print(pic.object_array)

mean_resized = cv.resize(pic.mean_array, [500,500], interpolation = cv.INTER_AREA)

cv.imshow("mean resized", mean_resized)
cv.imshow("img",pic.img)
cv.waitKey()
cv.destroyAllWindows()

