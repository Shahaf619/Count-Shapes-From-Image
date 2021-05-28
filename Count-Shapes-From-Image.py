# import the necessary packages
import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt

#=======================================define blue_shapes function=======================================#
def blue_shapes (img) :
	# find all the 'blue' shapes in the image
	lower = np.array([255, 0, 0])
	upper = np.array([255, 125, 125])
	shapeMask = cv2.inRange(image, lower, upper)
	return shapeMask
#=========================================end blue_shapes function========================================#

#=======================================define red_shapes function========================================#
def red_shapes (img) :
	# find all the 'red' shapes in the image
	lower = np.array([0, 0, 255])
	upper = np.array([125, 125, 255])
	shapeMask = cv2.inRange(image, lower, upper)
	return shapeMask
#=========================================end red_shapes function============================================#

#=======================================define yellow_shapes function========================================#
def yellow_shapes (img) :
	# find all the 'yellow' shapes in the image
	lower = np.array([0, 240, 240])
	upper = np.array([0, 255, 255])
	shapeMask = cv2.inRange(image, lower, upper)
	return shapeMask
#=========================================end yellow_shapes function=========================================#

#========================================start count yellow shapes===========================================#
# path
path = r'C:\Users\USER\Desktop\Migal/image2.tif'

# Using cv2.imread() method
image = cv2.imread(path)

shapeMask = yellow_shapes (path)

#to find contours
contours,h = cv2.findContours(shapeMask,1,2)
pent = tri = sq = hc = cir = 0

# Loop and count shapes
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)

    if len(approx) == 3:
        tri += 1

    elif len(approx) == 4:
         sq += 1

    else:
         cir += 1

print ("yellow triangle = ", tri)
print ("yellow square = ", sq)
print ("yellow circle = ", cir)
#========================================end count yellow shapes===========================================#

#=========================================start count red shapes===========================================#
# convert image for distinguish color
shapeMask = red_shapes (path)

#to find contours
contours,h = cv2.findContours(shapeMask,1,2)
pent = tri = sq = hc = cir = 0

# Loop and count shapes
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)

    if len(approx) == 3:
        tri += 1

    elif len(approx) == 4:
         sq += 1

    else:
         cir += 1

print ("red triangle = ", tri)
print ("red square = ", sq)
print ("red circle = ", cir)
#========================================end count red shapes=============================================#

#=========================================start count blue shapes===========================================#
# convert image for distinguish color
shapeMask = blue_shapes (path)

#to find contours
contours,h = cv2.findContours(shapeMask,1,2)
pent = tri = sq = hc = cir = 0

# Loop and count shapes
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)

    if len(approx) == 3:
        tri += 1

    elif len(approx) == 4:
         sq += 1

    else:
         cir += 1

print ("blue triangle = ", tri)
print ("blue square = ", sq)
print ("blue circle = ", cir)
#========================================end count red shapes=============================================#
