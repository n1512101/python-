import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
img = cv2.imread("1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale(gray)
for x,y,w,h in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
    id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

    for roots, dirs, files in os.walk("face_data"):
        for dir_name in dirs:
            if str(id) == dir_name.split(".")[0]:
                global name
                name = dir_name.split(".")[1]

    cv2.putText(img, name, (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
    print("idは:", id, "評価は:", confidence)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()