import cv2 as cv

# 顔識別関数
def face_detect_demo(img):
    gray_face = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")
    faces = face_detect.detectMultiScale(gray_face)
    for x,y,w,h in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv.imshow("result", img)

cap = cv.VideoCapture(0)

# 画像表示をキープ  'q'を押すと終了
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord('q') == cv.waitKey(10):
        break

# 画像を閉じる
cv.destroyAllWindows()

cap.release()