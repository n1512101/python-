import numpy as np

t = np.arange(24).reshape((4,6))
print(t)
print('-'*50)

# print(t[t<10])
# print('-'*50)

# t[t<10] = 0
# print(t)

# print(np.where(t<10,0,100))

print(t.clip(10,18))