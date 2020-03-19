import cv2
import numpy as n
#linear scaling
img=cv2.imread('df.jpg')
height,width=img.shape[:2]
img_scaled=cv2.resize(img,None,fx=0.5,fy=0.5)
img_scaled1=cv2.resize(img,None,fx=.8,fy=.8,interpolation=cv2.INTER_CUBIC)
img_scaled2=cv2.resize(img,(600,600),interpolation=cv2.INTER_AREA)
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Linear Scaling',img_scaled)
cv2.waitKey(0)
cv2.imshow('Cubic scaling',img_scaled1)
cv2.waitKey(0)
cv2.imshow('Area Scaling',img_scaled2)
cv2.imwrite('df1.jpg',img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()