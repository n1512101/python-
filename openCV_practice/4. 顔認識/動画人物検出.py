from pathlib import Path
import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
face_detector = cv2.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, maxSize=(300,300), minSize=(80,80))
    for x,y,w,h in faces:
        
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
        if confidence < 85:
            for roots, dirs, files in os.walk("face_data"):
                for dir_name in dirs:
                    if str(id) == dir_name.split(".")[0]:
                        global name
                        name = dir_name.split(".")[1]


            
            cv2.putText(frame, name, (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
            print("名前は:", name, "評価は:", confidence)

        




    if not ret or frame is None:
        print("Error: Failed to retrieve frame.")
        break

    cv2.imshow("result", frame)

    if cv2.waitKey(10) == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()