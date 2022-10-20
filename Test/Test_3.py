# #Edge detection test
# #If statement som
from mimetypes import guess_all_extensions
import cv2 as cv

import numpy as np

# board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)
# # Temporary images for each color channel
# b = cv.CreateImage(cv.GetSize(board_4), board_4.depth, 1)
# g = cv.CloneImage(b)
# r = cv.CloneImage(b)
# cv.Split(board_4, b, g, r, None)

# # Threshold each channel using individual lo and hi thresholds
# channels = [ b, g, r ]
# thresh = [ (100, 110), (50, 200), (70, 120) ]
# for c, (lo, hi) in zip(channels, thresh):
#     cv.Threshold(ch, ch, hi, 100, cv.CV_THRESH_TOZERO_INV)
#     cv.Threshold(ch, ch, lo, 100, cv.CV_THRESH_TOZERO)

# # Compose a new RGB image from the thresholded channels (if you need it)
# dst = cv.CloneImage(board_4)
# cv.Merge(b, g, r, None, dst)

board_4 = cv.imread(r"King Domino dataset\Cropped and perspective corrected boards\4.jpg", 1)

b,g,r = cv.split(board_4)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
cv.waitKey(0)






