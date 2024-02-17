# sorted
lst = [54,56,2,456,11]
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)
print(asc_lst, desc_lst)

# reversed
new_lst = reversed(lst)
print(new_lst)
print(list(new_lst))

# zip
x = ['a', 'b', 'c', 'd']
y = [10,20,30,40,50]
zipobj = zip(x,y)
print(type(zipobj))
# print(list(zipobj))

# enumerate
enum = enumerate(y, start=3)
print(type(enum))
print(tuple(enum))

# all
lst2 = [10,20,'',30]
print(all(lst2))
print(all(lst))

# any
print(any(lst2))

# next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))

# filter
def fun(num):
    return num%2==1

obj= filter(fun, range(10))
print(list(obj))

# map
def upper(x):
    return x.upper()

lst3 = ['hello', 'world', 'python']
obj2=map(upper, lst3)
print(list(obj2))