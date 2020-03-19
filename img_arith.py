import cv2
import numpy as aalok
img=cv2.imread('df1.jpg')
M=aalok.ones(img.shape,dtype="uint8")*20
add=cv2.add(img,M)
Sub=cv2.subtract(img,M)
mul=cv2.multiply(img,M)
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Added',add)
cv2.waitKey(0)
cv2.imshow('Subtracted',Sub)
cv2.waitKey(0)
cv2.imshow('Multiplied',mul)
cv2.waitKey(0)
cv2.destroyAllWindows()