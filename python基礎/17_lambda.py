def calc(a,b):
    return a+b

print(calc(10,20))

result = lambda a,b:a+b
print(type(result))
print(result(10,20))