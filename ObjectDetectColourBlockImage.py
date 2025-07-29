# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:16:34 2025

@author: G00397054@atu.ie
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:31:03 2021

@author: Dan Koskiranta
"""
import cv2 as cv
import numpy as np

# Create an image
image = np.zeros((400, 400, 3), np.uint8)  #creates a 400x400x3 array of ZEROS
# Add code to create an image with red, blue, red & yellow squares
image[100:200, 100:200] = (0, 0, 255) #red BGR order
image[100:200, 100:200] = (255, 0, 0) #blue
image[200:300, 200:300] = (0, 255, 0) #green
image[200:300, 200:300] = (0, 255, 255) #yellow
# Plot image
cv.imshow('Input Image', image)
cv.waitKey(0)


# Convert to HSV colour model
image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)# Add code, use opencv's cvtColor function

                         
#Note Blue is at ~120 degrees on the 
# Create mask
# Note: green hue 60, Blue hue 120, Yellow hue 30, Red hue 0
lower = np.array([110, 0, 0])
upper = np.array([130, 255, 255])
mask = cv.inRange(image_hsv, lower, upper)

#cv.bitwise_and(image, image, mask=mask)
image_out = cv.bitwise_and(image, image, mask=mask)

# Note: green hue 60, Blue hue 120, Yellow hue 30, Red hue 0
#lower = # Add code to create an array with BGR colours for lower threshold
#upper = # Add code to create an array with BGR colours for upper threshold
#mask = cv.inRange(image_hsv, lower, upper)

# Apply mask to input image to get ouput image
# Add code to create outpu image, use cv.bitwise_and(image, image, mask=mask)

# Plot mask & output image
cv.imshow('Mask', mask)
cv.waitKey(0)

cv.imshow('Output Image', image_out)
cv.waitKey(0)
