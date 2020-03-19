import cv2
import numpy as n
camera = cv2.imread('df1.jpg')
face_class = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_class = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_class = cv2.CascadeClassifier('haarcascade_smile.xml')
gray = cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
faces = face_class.detectMultiScale(gray,1.3,10)

for(x,y,w,h) in faces:

    rect = cv2.rectangle(camera,(x,y),(x+w,y+h),(255,0,0),3)
    eyes=eye_class.detectMultiScale(gray,1.3,20)
    for(ex,ey,ew,eh) in eyes:
        centerx, centery = int((ex + ex + ew) / 2), int((ey + ey + eh) / 2)
        radius = int(eh / 2)
        rect = cv2.circle(camera,(centerx,centery),radius,(0,0,255),2)
    smiles = smile_class.detectMultiScale(gray, 1.3, 40)
    for(sx,sy,sw,sh) in smiles:
        rect = cv2.rectangle(camera, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)

rect=cv2.putText(rect,"Will you marry me ?",(50 ,50),cv2.FONT_HERSHEY_COMPLEX,1,(147,20,255),1)
cv2.imshow('Face',rect)
cv2.waitKey(0)
cv2.destroyAllWindows()