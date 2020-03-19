import cv2
import numpy as n
img=cv2.imread('df1.jpg')
blr_mat=n.ones((5,5),n.float)/25
blur=cv2.filter2D(img,-1,blr_mat)
cv2.imshow('Origial',img)
cv2.waitKey(0)
cv2.imshow('Blurrred',blur)
cv2.waitKey(0)

cv2.destroyAllWindows()