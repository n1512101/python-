class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'これは人間です。'
    
per = Person('cmm',39)
print(per)
print(per.__str__())