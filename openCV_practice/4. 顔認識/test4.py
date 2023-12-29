import cv2 as cv

# 画像読み取り
img = cv.imread("face2.jpg")

# 顔識別関数
def face_detect_demo():
    gray_face = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier("C:/Users/n1512/anaconda3/Lib/site-packages/opencv-4.8.0/data/haarcascades/haarcascade_frontalface_alt.xml")
    face = face_detect.detectMultiScale(gray_face, 1.1, 5)
    for x,y,w,h in face:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv.imshow("result", img)

# 関数を動作させる
face_detect_demo()

# 画像表示をキープ  'q'を押すと終了
while True:
    if ord('q') == cv.waitKey(0):
        break

# 画像を閉じる
cv.destroyAllWindows