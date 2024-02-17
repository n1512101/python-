import matplotlib.pyplot as plt

# 図形の大きさ
plt.figure(figsize=(14,6), dpi=80)

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,24,22,18,15,13]

# 横軸x,縦軸y
plt.plot(x,y)

# x,y軸座標の間隔調整
plt.xticks(x)
plt.yticks(range(min(y), max(y)+1))

# 図形を保存
plt.savefig('./t1.png')

# 図形を表示
plt.show()