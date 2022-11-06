import numpy as np
import cv2
import math

img = cv2.imread(r'King Domino dataset\Cropped and perspective corrected boards\4.jpg', 0)
template = cv2.imread(r'Detect_squares.py\Assests\castle_n_h_blue.png', 0)
h, w = template.shape

method = cv2.TM_CCOEFF_NORMED

img2 = img.copy()

result = cv2.matchTemplate(img2, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val)
print(math.isclose(max_val, 0.5, abs_tol = 0.2))

if math.isclose(max_val, 0.5, abs_tol=0.2) == True:
    print("Hello world!")

"""if
    location = min_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""