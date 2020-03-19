import cv2
import numpy as n
img=cv2.imread('df1.jpg',)
cv2.imshow('Originl',img)
cv2.waitKey(0)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey(0)
canny=cv2.Canny(img,100,250)
cv2.imshow('Canny',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()