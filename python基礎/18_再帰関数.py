def fun(n):
    if n==1:
        return 1
    else:
        return n * fun(n-1)
    
print(fun(5))

def fun2(n):
    if n==1 or n==2:
        return 1
    else:
        return fun2(n-1)+fun2(n-2)
    
print(fun2(9))