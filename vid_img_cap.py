import cv2
import matplotlib.pyplot as plot
camera=cv2.VideoCapture(0)
if camera.isOpened():
    ret,Frames=camera.read()
    print(ret)
    print(Frames)
else :
    ret=False
img1=cv2.cvtColor(Frames,cv2.COLOR_BGR2RGB)
plot.imshow(img1)
plot.title("Camera Image 1")
plot.xticks([])
plot.yticks([])
plot.show()
camera.release()
cv2.destroyAllWindows()