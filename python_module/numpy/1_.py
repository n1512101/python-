import numpy as np
import random

t1 = np.array([1,2,3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(4,10,2)
print(t3)
print(t3.dtype)

t4 = np.array(range(0,4), dtype=float)
print(t4)
print(t4.dtype)

t5 = np.array([0,1,1,0,1], dtype=bool)
print(t5)
print(t5.dtype)

t6 = t5.astype('int8')
print(t6)
print(t6.dtype)

t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

t8 = np.round(t7, 3)
print(t8)