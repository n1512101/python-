import cv2 as cv

# 画像読み取り
img = cv.imread("picture1.png")

# 色をグレーにする
gray_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# 画像を表示する
cv.imshow("gray", gray_img)

# 画像を表示する
cv.imshow("picture",img)

# 画像を保存する
cv.imwrite("gray_piecure1.png", gray_img)

# 画像表示をキープ
cv.waitKey(0)

# 画像を閉じる
cv.destroyAllWindows