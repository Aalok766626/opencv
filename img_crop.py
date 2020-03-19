import cv2
import numpy as n
img=cv2.imread('df1.jpg')
height,width=img.shape[:2]
start_row,start_col=int(height*0.25),int(width*0.15)
end_row,end_col=int (height*0.75),int (width*0.9)
cropped=img[start_row:end_row,start_col:end_col]
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.imshow('Cropped',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()