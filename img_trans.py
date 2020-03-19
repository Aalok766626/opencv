import cv2
import numpy as n
img=cv2.imread('df.jpg')
height,width=img.shape[:2]
h=height/10
w=width/10
Trans_mat=n.float32([[1,0,h],[0,1,w]])
img_trans=cv2.warpAffine(img,Trans_mat,(height,width))
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Translated',img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()