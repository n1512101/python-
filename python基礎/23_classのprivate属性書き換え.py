class Student:
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender
    
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, value):
        self.__gender =value

stu = Student('cmm', 'girl')
print(stu.name, stu.gender)

stu.gender = 'boy'
print(stu.name, stu.gender)