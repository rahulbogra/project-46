import cv2
#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture (0)
while True:
    isTrue, img = camera.read()
    faces = face_cascade.detectMultiScale(img, 1.5, 3,minSize=(30,30))

    for(x,y,w,h) in faces:
        cv2.rectangle (img, (x,y),(x+w,y+h),(255,255,0),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Human Face',(x,y-10),font,0.5,(0,0,255))

    cv2.imshow('Face Detection System',img)

    k = cv2.waitKey(1)
    if k == 27:
        break

camera.release()
cv2.destroyAllWindows()
