import matplotlib.pyplot as plt
import random

y = [random.randint(20,35) for i in range(120)]
x = range(0,120)

plt.figure(figsize=(14,6), dpi=80)

plt.plot(x,y)

_x = list(x)
_xticks_labels = ["10:{}".format(i) for i in range(60)]
_xticks_labels += ["11:{}".format(i) for i in range(60)]

plt.xticks(_x[::3], _xticks_labels[::3],rotation=45)
plt.yticks(range(0,max(y)+2,2))

# plt.savefig("./t2.png")

plt.xlabel('times')
plt.ylabel('temperature')
plt.title('temperature of 10-12')

plt.show()


