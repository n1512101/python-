import numpy as np

t1 = np.array(range(24))

t2 = t1.reshape((4,6))
# print(t2)
# print(t2+2)

t3 = np.arange(100,124).reshape((4,6))
# print(t3)
# print(t2+t3)

t4 = np.arange(6)
# print(t3-t4)

t5 = np.arange(24).reshape(4,6)
# print(t5)
# print(t5.transpose())     # 倒置関数
# print(t5.T)                 # 倒置関数