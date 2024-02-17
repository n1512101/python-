t = ('hello', 'python', 'world')
print(t)

t=tuple('helloworld')
print(t)

t=tuple([1,2,3,4])
print(t)

print(1 in t)
print(1 not in t)
print(max(t), min(t), len(t))
print(t.index(3))
print(t.count(2))

t=(10)
print(t, type(t))

y=(10,)
print(y, type(y))

del t
# print(t)