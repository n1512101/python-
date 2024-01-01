import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
face_detector = cv2.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture("ikeda.mp4")

while True:
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        cv2.putText(frame, str(id), (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
        print("idは:", id, "評価は:", confidence)



    if not ret or frame is None:
        print("Error: Failed to retrieve frame.")
        break

    cv2.imshow("result", frame)

    if cv2.waitKey(10) == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()