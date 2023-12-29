def fn(n):
    return n ** 2

print(fn(3))

#　匿名関数    lambda 引数 : 式
demo = lambda n:n ** 2
print(demo(5))


def add(a,b):
    print(a + b)


def common(a,b,func):
    func(a,b)

common(5,6,add)