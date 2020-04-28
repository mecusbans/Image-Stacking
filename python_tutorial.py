# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:28:51 2020

@author: Clinton
"""


import cv2
import numpy as np

width , height = 1000, 1000

img_path = "F:/opencv_learning/image_file/runner.jpg"
img = cv2.imread(img_path) #Reading image
print(img.shape)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting image from color to gray scale
img_resized = cv2.resize(img, (width, height)) #Resizing image
img_cropped = img[0:469, 160:510] #Cropping Image
imgCroppedResized = cv2.resize(img_cropped, (img.shape[1], img.shape[0])) #Resizing cropped image back to the original size


scale = 0.8
img = cv2.resize(img, (400, 400), None, scale, scale)
img_resized = cv2.resize(img_resized, (400, 400), None, scale, scale)
img_cropped = cv2.resize(img_cropped, (400, 400), None, scale, scale)
imgCroppedResized = cv2.resize(imgCroppedResized, (400, 400), None, scale, scale)

#Blank Image
imgBlank = np.zeros((400,400), np.uint8)
imgBlank = cv2.cvtColor(imgBlank, cv2.COLOR_GRAY2BGR)


hori_image1 = np.hstack((img, img_resized, imgBlank))
hori_image2 = np.hstack((imgBlank, img_cropped, imgCroppedResized))
vertical_image = np.vstack((hori_image1, hori_image2))


cv2.imshow('Runner Image', vertical_image)

 

# cv2.imshow("Original Image", img)
# cv2.imshow("Gray Scale Image", img_gray)
# cv2.imshow("Resized Image", img_resized)
# cv2.imshow("Cropped Image", img_cropped)
# cv2.imshow("Runner_CroppedResized", imgCroppedResized)

cv2.waitKey(0)
cv2.destroyAllWindows()