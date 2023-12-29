# def demo(name, age):
#     print("my name is %s, I am %d"%(name, age))

# demo("Jack", 26)
# demo(age=19, name="Tom")


# def sum(num1 = 13, num2 = 10):
#     print(num1 + num2)

# sum(2,40)
# sum(2)
# sum()


# 引数*args
def fn(*args):
    print(args)

fn(33,11,44)
fn()
fn(11)
fn("abc",11)


# 引数 **kwargs
def fn2(**kwargs):
    print(kwargs)

fn2(x = 13, y = 30)