import numpy as np 
import cv2 as cv
import statistics as sta
import math 

class image_handler():
    def __init__(self):
        self.img = cv.imread(r"King Domino dataset/Cropped and perspective corrected boards/21.jpg",1)
        self.board_size = 5
        self.point_counter = 0
        self.crowns_made = [(-500,-500)]
        self.b = 0
        self.threshold = 0.6

    def find_crown_location(self, location):
        input_crown_location = 0
        print("crowns made",self.crowns_made)
        for i in range(len(self.crowns_made)):
            
            if location[0] < self.crowns_made[i][0]-5 or location[1] < self.crowns_made[i][1]-5 and location[0] > self.crowns_made[i][0]+5 or location[1] > self.crowns_made[i][1]+5:
                #print("crown0,crown1",self.crowns_made[i][0],self.crowns_made[i][1], "location0 og 1", location[0],location[1])
                self.b += 1
                print("b = ", self.b, "  i = ", i)
                if location[0] > 0 and location[0] < 100 and location[1] > 0 and location[1] < 100:
                    input_crown_location = [0,0]
                elif location[0] > 100 and location[0] < 200 and location[1] > 0 and location[1] < 100:
                    input_crown_location = [0,1]
                elif location[0] > 200 and location[0] < 300 and location[1] > 0 and location[1] < 100:
                    input_crown_location = [0,2]
                elif location[0] > 300 and location[0] < 400 and location[1] > 0 and location[1] < 100:
                    input_crown_location = [0,3]
                elif location[0] > 400 and location[0] < 500 and location[1] > 0 and location[1] < 100:
                    input_crown_location = [0,4]
                
                elif location[0] > 0 and location[0] < 100 and location[1] > 100 and location[1] < 200:
                    input_crown_location = [1,0]
                elif location[0] > 100 and location[0] < 200 and location[1] > 100 and location[1] < 200:
                    input_crown_location = [1,1]
                elif location[0] > 200 and location[0] < 300 and location[1] > 100 and location[1] < 200:
                    input_crown_location = [1,2]
                elif location[0] > 300 and location[0] < 400 and location[1] > 100 and location[1] < 200:
                    input_crown_location = [1,3]
                elif location[0] > 400 and location[0] < 500 and location[1] > 100 and location[1] < 200:
                    input_crown_location = [1,4]

                elif location[0] > 0 and location[0] < 100 and location[1] > 200 and location[1] < 300:
                    input_crown_location = [2,0]
                elif location[0] > 100 and location[0] < 200 and location[1] > 200 and location[1] < 300:
                    input_crown_location = [2,1]
                elif location[0] > 200 and location[0] < 300 and location[1] > 200 and location[1] < 300:
                    input_crown_location = [2,2]
                elif location[0] > 300 and location[0] < 400 and location[1] > 200 and location[1] < 300:
                    input_crown_location = [2,3]
                elif location[0] > 400 and location[0] < 500 and location[1] > 200 and location[1] < 300:
                    input_crown_location = [2,4]

                elif location[0] > 0 and location[0] < 100 and location[1] > 300 and location[1] < 400:
                    input_crown_location = [3,0]
                elif location[0] > 100 and location[0] < 200 and location[1] > 300 and location[1] < 400:
                    input_crown_location = [3,1]
                elif location[0] > 200 and location[0] < 300 and location[1] > 300 and location[1] < 400:
                    input_crown_location = [3,2]
                elif location[0] > 300 and location[0] < 400 and location[1] > 300 and location[1] < 400:
                    input_crown_location = [3,3]
                elif location[0] > 400 and location[0] < 500 and location[1] > 300 and location[1] < 400:
                    input_crown_location = [3,4]
                
                elif location[0] > 0 and location[0] < 100 and location[1] > 400 and location[1] < 500:
                    input_crown_location = [4,0]
                elif location[0] > 100 and location[0] < 200 and location[1] > 400 and location[1] < 500:
                    input_crown_location = [4,1]
                elif location[0] > 200 and location[0] < 300 and location[1] > 400 and location[1] < 500:
                    input_crown_location = [4,2]
                elif location[0] > 300 and location[0] < 400 and location[1] > 400 and location[1] < 500:
                    input_crown_location = [4,3]
                elif location[0] > 400 and location[0] < 500 and location[1] > 400 and location[1] < 500:
                    input_crown_location = [4,4]

        return(input_crown_location)
    
    def find_crown_meadow(self):
         #This is for the crown_meadow in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_meadow = cv.imread(r"Detect_squares.py/Assests/crown_meadow.jpg", 0)
    
        method =  cv.TM_CCORR_NORMED
        w, h = self.crown_meadow.shape
        
        
        
        for i in range(4):
            if i > 0: 
                self.crown_meadow = cv.rotate(self.crown_meadow, cv.ROTATE_90_CLOCKWISE)
            gray_copy = self.gray.copy()
            res = cv.matchTemplate(gray_copy, self.crown_meadow, method)
            location = np.where (res >= self.threshold)
            #res = cv.matchTemplate(gray_copy, self.crown_meadow, method)
            #min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
            #location = max_loc
            #if math.isclose(self.max_val, 1, abs_tol=0.01) == True:
            bottom_right = (location[0] + w, location[1] + h)
            self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
            self.crowns_made.append(location)
            input_crown_location = self.find_crown_location(location)
            self.locate_connections(input_crown_location)
            
    def find_crown_swamp(self):
        #This is for the crown_swamp in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_swamp = cv.imread(r"Detect_squares.py/Assests/crown_swamp.png", 0)

        method =  cv.TM_CCORR_NORMED
        h, w = self.crown_swamp.shape
        for i in range(4):
            if i > 0: 
                self.crown_swamp = cv.rotate(self.crown_swamp, cv.ROTATE_90_CLOCKWISE)
            gray_copy = self.gray.copy()
            res = cv.matchTemplate(gray_copy, self.crown_swamp, method)
            min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
            location = max_loc
            if math.isclose(self.max_val, 1, abs_tol=0.013) == True:
                bottom_right = (location[0] + w, location[1] + h)
                self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                self.crowns_made.append(location)
                input_crown_location = self.find_crown_location(location)
                self.locate_connections(input_crown_location)
          
    def find_crown_forrest(self):
        #This is for the crown_forrest in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_forrest = cv.imread(r"Detect_squares.py/Assests/crown_mine.png", 0)

        method =  cv.TM_CCORR_NORMED
        h, w = self.crown_forrest.shape
        for i in range(4):
                if i > 0: 
                    self.crown_forrest = cv.rotate(self.crown_forrest, cv.ROTATE_90_CLOCKWISE)
                gray_copy = self.gray.copy()
                res = cv.matchTemplate(gray_copy, self.crown_forrest, method)
                min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
                location = max_loc
                if math.isclose(self.max_val, 1, abs_tol=0.02) == True:
                    bottom_right = (location[0] + w, location[1] + h)
                    self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                    self.crowns_made.append(location)
                    input_crown_location = self.find_crown_location(location)
                    self.locate_connections(input_crown_location)
                    
    def find_crown_mine(self):
        #This is for the crown_mine in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_mine = cv.imread(r"Detect_squares.py/Assests/crown_mine.png", 0)

        method = cv.TM_CCORR_NORMED
        h, w = self.crown_mine.shape
        for i in range(4):
            if i > 0: 
                self.crown_mine = cv.rotate(self.crown_mine, cv.ROTATE_90_CLOCKWISE)
            gray_copy = self.gray.copy()
            res = cv.matchTemplate(gray_copy, self.crown_mine, method)
            min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
            location = max_loc
            if math.isclose(self.max_val, 1, abs_tol=0.03) == True:
                bottom_right = (location[0] + w, location[1] + h)
                self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                self.crowns_made.append(location)
                input_crown_location = self.find_crown_location(location)
                self.locate_connections(input_crown_location)
          
    def find_crown_corn(self):
        #This is for the crown_corn in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_corn = cv.imread(r"Detect_squares.py/Assests/crown_corn.png", 0)

        method =  cv.TM_CCORR_NORMED
        h, w = self.crown_corn.shape
        for i in range(4):
            if i > 0: 
                self.crown_corn = cv.rotate(self.crown_corn, cv.ROTATE_90_CLOCKWISE)
            gray_copy = self.gray.copy()
            res = cv.matchTemplate(gray_copy, self.crown_corn, method)
            min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
            location = max_loc
            if math.isclose(self.max_val, 1, abs_tol=0.002) == True:
                bottom_right = (location[0] + w, location[1] + h)
                self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                self.crowns_made.append(location)
                input_crown_location = self.find_crown_location(location)
                self.locate_connections(input_crown_location)
                                  
    def find_crown_ocean(self):
        #This is for the crown_ocean in all rotations
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.crown_ocean = cv.imread(r"Detect_squares.py/Assests/crown_ocean.png", 0)
        method =  cv.TM_CCORR_NORMED
        h, w = self.crown_ocean.shape
        for i in range(4):
            if i > 0: 
                self.crown_ocean = cv.rotate(self.crown_ocean, cv.ROTATE_90_CLOCKWISE)
            gray_copy = self.gray.copy()
            res = cv.matchTemplate(gray_copy, self.crown_ocean, method)
            min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
            location = max_loc
            if math.isclose(self.max_val, 1, abs_tol=0.02) == True:
                bottom_right = (location[0] + w, location[1] + h)
                self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                self.crowns_made.append(location)
                input_crown_location = self.find_crown_location(location)
                self.locate_connections(input_crown_location)
           
    def find_tower(self):#Function to find the tower and change the color values to 0 to locate it easier.
        #This is for blue castles with no house but kinda works for green and pink as well
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.template_tower_n_h = cv.imread(r"Detect_squares.py/Assests/castle_n_h_blue_rotated.png", 0)#tower with no house on.
        methods =  [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF]
        h, w = self.template_tower_n_h.shape
        for i in range(4):
            for method in methods:
                if i > 0: 
                    self.template_tower_n_h = cv.rotate(self.template_tower_n_h, cv.ROTATE_90_CLOCKWISE)
                gray_copy = self.gray.copy()
                res = cv.matchTemplate(gray_copy, self.template_tower_n_h, method)
                min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    location = min_loc
                else: 
                    location = max_loc
                if math.isclose(self.max_val, 1, abs_tol=0.01) == True:
                    bottom_right = (location[0] + w, location[1] + h)
                    self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                
        #This is for yellow castles with no house
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.template_tower_n_h = cv.imread(r"Detect_squares.py/Assests/castle_n_h_yellow.png", 0)#tower with no house on.
        methods =  [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF]
        h, w = self.template_tower_n_h.shape
        for i in range(4):
            for method in methods:
                if i > 0: 
                    self.template_tower_n_h = cv.rotate(self.template_tower_n_h, cv.ROTATE_90_CLOCKWISE)
                gray_copy = self.gray.copy()
                res = cv.matchTemplate(gray_copy, self.template_tower_n_h, method)
                min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    location = min_loc
                else: 
                    location = max_loc
                if math.isclose(self.max_val, 1, abs_tol=0.015) == True:
                    bottom_right = (location[0] + w, location[1] + h)
                    self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                
         #This is for green castles with no house
        self.gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        self.template_tower_n_h = cv.imread(r"Detect_squares.py/Assests/castle_n_h_green.png", 0)#tower with no house on.
        methods =  [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR,
            cv.TM_CCORR_NORMED, cv.TM_SQDIFF]
        h, w = self.template_tower_n_h.shape
        for i in range(4):
            for method in methods:
                if i > 0: 
                    self.template_tower_n_h = cv.rotate(self.template_tower_n_h, cv.ROTATE_90_CLOCKWISE)
                gray_copy = self.gray.copy()
                res = cv.matchTemplate(gray_copy, self.template_tower_n_h, method)
                min_val, self.max_val, min_loc, max_loc = cv.minMaxLoc(res)
                if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
                    location = min_loc
                else: 
                    location = max_loc
                if math.isclose(self.max_val, 1, abs_tol=0.015) == True:
                    bottom_right = (location[0] + w, location[1] + h)
                    self.img = cv.rectangle(self.img, location, bottom_right, 0, -1)
                
    def mean_cal(self):
        self.mean_array = np.zeros((5, 5, 3), dtype='uint8')
        for j in range(self.board_size):
            for i in range(self.board_size):
                b_mean = []
                g_mean = []
                r_mean = []
                for y in range(j*100, 100+j*100):
                    for x in range(i*100, 100+i*100): 
                        #print(x,y) 
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
        tower = 8
        th_corn = [(0,31),(110,178),(130,220)]
        th_ocean = [(90,210),(46,150),(0,70)]
        th_meadow = [(7,51),(60,160),(51,145)]
        th_forrest = [(7,100),(34,80),(25,80)]
        th_mine = [(30,47),(53,76),(60,92)]
        th_swamp = [(41,100),(70,127),(84,133)]
        th_tower = [(0,20),(0,20),(0,20)]
        self.landscape_map = np.zeros((5, 5), dtype="U")
        self.area_map = np.zeros((5, 5),dtype="uint8")
        for j in range(self.board_size):
            for i in range(self.board_size):
                b,g,r = self.mean_array[i,j]
                #print(i,j)
                #print(self.mean_array[i,j])
                if b < th_tower[0][1] and g < th_tower[1][1] and r < th_tower[2][1]:
                    self.landscape_map[i,j] = "tower"
                    self.area_map[i,j] = tower
                elif b >= th_corn[0][0] and b <= th_corn[0][1] and g >= th_corn[1][0] and g <= th_corn[1][1] and r >= th_corn[2][0] and r <= th_corn[2][1]:
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
                    if abs(g-r) <= 20 and b <= 40 and g < 100: 
                        self.landscape_map[i,j] = "forrest"
                        self.area_map[i,j] = forrest
                    elif g < r: 
                        if r - g > 30: 
                            self.landscape_map[i,j] = "not figured"
                            self.area_map[i,j] = not_figured
                        elif b >= th_mine[0][0] and b <= th_mine[0][1] and g >= th_mine[1][0] and g <= th_mine[1][1] and r >= th_mine[2][0] and r <= th_mine[2][1]:
                            self.landscape_map[i,j] = "digging"
                            self.area_map[i,j] = digging
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
                    if r > 3+g: 
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

    def locate_connections(self, input_crown_location):
        self.object_array = np.zeros((5, 5), dtype="uint8") 
        print("input_crown = ", input_crown_location)
        if type(input_crown_location) == list: 
            a = 0
            for i in range(self.board_size):
                for j in range(self.board_size):
                    if self.area_map[i,j] == self.area_map[input_crown_location[0], input_crown_location[1]]:
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
                    
        
            count_1 = np.count_nonzero(self.object_array == 1)
            count_2 = np.count_nonzero(self.object_array == 2)
            count_3 = np.count_nonzero(self.object_array == 3)
            count_4 = np.count_nonzero(self.object_array == 4)
            count_5 = np.count_nonzero(self.object_array == 5)
            count_6 = np.count_nonzero(self.object_array == 6)
            """print('Total occurences of "1" in array: ', count_1)
            print('Total occurences of "2" in array: ', count_2)
            print('Total occurences of "3" in array: ', count_3)
            print('Total occurences of "4" in array: ', count_4)
            print('Total occurences of "5" in array: ', count_5)
            print('Total occurences of "6" in array: ', count_6)"""
        
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 1: 
                self.point_counter = self.point_counter + count_1 
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 2: 
                self.point_counter = self.point_counter + count_2 
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 3: 
                self.point_counter = self.point_counter + count_3 
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 4: 
                self.point_counter = self.point_counter + count_4 
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 5: 
                self.point_counter = self.point_counter + count_5 
            if self.object_array[input_crown_location[0],input_crown_location[1]] == 6: 
                self.point_counter = self.point_counter + count_6
            print(self.object_array)
            print("points  =   ",  self.point_counter)
            
image_test = image_handler()
image_test.find_tower()
image_test.mean_cal()
image_test.find_landscape()
image_test.find_crown_ocean()
image_test.find_crown_corn()
image_test.find_crown_forrest()
image_test.find_crown_mine()
image_test.find_crown_swamp()
image_test.find_crown_meadow()
print("points = ", image_test.point_counter)

image = image_handler()#Desplays the normal picture

print(image_test.landscape_map)


mean_resized = cv.resize(image_test.mean_array, [500,500], interpolation = cv.INTER_AREA)

cv.imshow("mean resized", mean_resized)
cv.imshow("img",image_test.img)
cv.imshow("img no change", image.img)
cv.waitKey()
cv.destroyAllWindows()