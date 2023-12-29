import cv2 as cv

# 画像読み取り
img = cv.imread("face1.jpg")

# サイズ変更
resize_img = cv.resize(img, dsize=(630,500))

# 画像表示
cv.imshow("img", img)
cv.imshow("resize_img", resize_img)

# 画像サイズを表示
print("imgのサイズ:", img.shape)
print("resize_imgのサイズ:", resize_img.shape)

# 画像表示をキープ  'q'を押すと終了
while True:
    if ord('q') == cv.waitKey(0):
        break

cv.imwrite("face2.jpg", resize_img)

# 画像を閉じる
cv.destroyAllWindows