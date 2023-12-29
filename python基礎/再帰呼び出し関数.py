def saiki(n):
    if n == 1:
        return 1
    return n * saiki(n-1)

print(saiki(5))


def fn(m):
    if m < 3 :
        return 1
    return fn(m-1)+fn(m-2)

print(fn(11))