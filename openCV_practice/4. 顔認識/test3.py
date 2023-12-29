import cv2 as cv

# 画像読み取り
img = cv.imread("picture1.png")

# 四角を書く
cv.rectangle(img, (100,100), (200,200), (0,0,255), 2)

# 円を描く
cv.circle(img, (100,300), 50, (0,255,200), 2)

# 画像を表示
cv.imshow("img", img)

# 画像表示をキープ  'q'を押すと終了
while True:
    if ord('q') == cv.waitKey(0):
        break

# 画像を閉じる
cv.destroyAllWindows