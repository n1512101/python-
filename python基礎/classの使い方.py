# class Dog():
#     name = "Bob"

#     def say(self):
#         print("ワン")

# dog = Dog()
# print(dog.name)
# dog.say()

class Student():
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(self.name, "走っている")

    def eat(self):
        print(self.name, "食べている")
    
stu1 = Student("Jerry", 29)
stu1.run()

stu2 = Student("Tom",30)
stu2.eat()
