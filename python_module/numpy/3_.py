import numpy as np

us_file_path = './files/usa.csv'
uk_file_path = './files/uk.csv'

# t1 = np.loadtxt(us_file_path, delimiter=',',dtype='int',unpack=True)  # unpack=True 倒置関数になる
t2 = np.loadtxt(us_file_path, delimiter=',',dtype='int')
# print(t1)
# print('-'*100)
print(t2)
print('-'*100)
# print(t2[2])
# print(t2[[2,8,10]])    # 複数行を取り出す

# print(t2[1,1:])
# print(t2[:,0])
# print(t2[:,[1,3]])
# print(t2[2,3])
# print(t2[3:6,2:5])
# print(t2[[0,2],[0,1]])
