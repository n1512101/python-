def fun(*person):
    print(type(person))
    for i in person:
        print(i)
        
fun(10,20,30,40)
fun([11,22,33,44])
fun(*[11,22,33,44])

def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key, '-->', value)
        
fun2(name='jerry', age=18, height=170)

dict = {'name':'jerry', 'age':18, 'height':170}
fun2(**dict)