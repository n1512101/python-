import numpy
import cv2
import matplotlib.pyplot as plt

# 画像を定義する
img = numpy.zeros((512, 512, 3), numpy.uint8)

# 画像を編集する
cv2.line(img, (0,0), (511,511), (255,0,0), 5)  # 直線
cv2.circle(img, (256,256), 60, (0,0,255), -1)  # 円
cv2.rectangle(img, (100,100), (400,400), (0,255,0), 4)  # 正方形
cv2.putText(img, "hello", (100,150), cv2.FONT_HERSHEY_COMPLEX, 5, (255,255,255), 3)  # 文字を書き込む


# 画像を表示
plt.imshow(img[:,:,::-1])
plt.show()