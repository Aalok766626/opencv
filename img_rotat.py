import cv2
import numpy as n
img=cv2.imread('df.jpg')
height,width=img.shape[:2]
rotat_mat=cv2.getRotationMatrix2D((width/2,height/2),50,0.45)
rotated_image=cv2.warpAffine(img,rotat_mat,(height,width))
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Rotated',rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()