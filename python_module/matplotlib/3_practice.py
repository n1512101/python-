import matplotlib.pyplot as plt

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x = range(11,31)

plt.figure(figsize=(14,6), dpi=80)

_xticks_label = ["{}y".format(i) for i in x]

plt.xticks(x,_xticks_label)
plt.yticks(range(9))

plt.plot(x,y_1,label='Jerry')
plt.plot(x,y_2,label='Tom')

plt.grid(alpha = 0.4)

plt.legend(loc=2)

plt.show()