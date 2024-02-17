import numpy as np
import matplotlib.pyplot as plt

picture = plt.imread('C:/Users/n1512/Desktop/Python/openCV_practice/4. 顔認識/face_data/9.sumi/1.jpg')
print(picture)
print(type(picture))


picture2 = np.array([0.299, 0.587, 0.114])
x=np.dot(picture, picture2)
plt.imshow(x, cmap='gray')
plt.show()
