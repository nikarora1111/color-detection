import cv2
import numpy as np
imgpath="C:\\Users\\ARORA\\Desktop\\standard_test_images\\peppers_color.tif"
img = cv2.imread(imgpath)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([170,100,100])
upper_red1 = np.array([179,255,255])
lower_red2 = np.array([0,100,100])
upper_red2= np.array([10,255,255])
lower_mask = cv2.inRange(hsv, lower_red1, upper_red1)
upper_mask = cv2.inRange(hsv, lower_red2, upper_red2)
mask=lower_mask+upper_mask
res = cv2.bitwise_and(img,img, mask= mask)
cv2.imshow('image',img)
cv2.imshow('mask',mask)
cv2.imshow('result',res)
cv2.waitKey(0)
cv2.destroyAllWindows()