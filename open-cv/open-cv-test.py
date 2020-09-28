# Import libraries
import cv2
import os

# Reading the image with opencv
FILEPATH = '/Users/javiervinas/Documents/Bootcamp_Data/final_project_ironhack/facturas/factura_mayo_image.jpg'

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
img = cv2.imread(FILEPATH)
img_resized = cv2.resize(img, (960, 540))
cv2.imshow("Output4", img_resized)
cv2.waitKey(0)