import cv2

face = cv2.CascadeClassifier("haarcascade_frontalface_defau1t.xm1")
img = cv2.imread("")

faceRects = face.detectMultiScale(
    img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(100,100),
    maxSize=(200,200)
)
print(faceRects,type(faceRects))
cv2.rectangle(img, (0, 0), (140, 20), (0, 255, 255), -1)
cv2.putText(img, "Finding" + str(len(faceRects)) + " face",(3,15),
            cv2.Font_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
for x, y, w, h in faceRects:
    cv2.rectangle(img, (x,y),(x + w, y + h),(0,0,255),1)
cv2.imshow("image", img)
cv2.waitKey()
cv2.distroyALLWindows()