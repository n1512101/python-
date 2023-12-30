import cv2 as cv


def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255),3)
    cv.imshow("result", img)



cap = cv.VideoCapture(0)

while True:
    flag, frame = cap.read()

    if not flag:
        break

    face_detect_demo(frame)

    if cv.waitKey(10) == ord('q'):
        break

cv.destroyAllWindows()
cap.release()