class Animal():
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def eat(self):
        print("食べている")

class Dog(Animal):
    def run(self):
        print("走っている")

dog = Dog("犬", "boy")
dog.run()
print(dog.name)
