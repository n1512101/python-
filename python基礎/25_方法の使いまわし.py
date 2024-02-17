class Person():
    def eat(self):
        print('米を食べる')

class Cat():
    def eat(self):
        print('魚を食べる')
        
class Dog():
    def eat(self):
        print('骨を食べる')

def fun(obj):
    obj.eat()
    
per = Person()
cat = Cat()
dog = Dog()

fun(per)
fun(cat)
fun(dog)