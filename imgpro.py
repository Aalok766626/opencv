import cv2
img = cv2.imread('df.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)
black=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',black)
cv2.waitKey(0)
print(img.shape)
ret, gray= cv2.threshold(black,127,255,cv2.THRESH_BINARY)
cv2.imshow('black',gray)
cv2.waitKey(0)
height,width=img.shape[:2]
print(height,width)
ret, n1=cv2.threshold(black,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Aalok',n1)
cv2.waitKey(0)
img=cv2.rectangle(img,(20,20),(50,50),(255,0,0),5)
cv2.imshow('Rect',img)
cv2.waitKey(0)
cv2.destroyAllWindows()