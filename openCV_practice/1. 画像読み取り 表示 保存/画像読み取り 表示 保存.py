import cv2
import numpy
import matplotlib.pyplot as plt

# 画像読み取り cv2.imread()
lena = cv2.imread("picture1.png")
# lena = cv2.imread("picture1.png", 0)    # 白黒写真


# # opencvを用いた画像の表示  cv2.imshow() 後ろにcv2.waitKey()が必要
# cv2.imshow("image", lena)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# matplotlibを使う
plt.imshow(lena[:, :, ::-1])
# plt.imshow(lena, cmap=plt.cm.gray)   # 白黒写真
plt.show()


# 画像を保存
cv2.imwrite("picture2.png", lena)