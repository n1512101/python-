class Student():
    def __init__(self,name,age,gender):
        self._name = name
        self.__age = age
        self.gender = gender
    
    def _fun1(self):
        print('one _')
        
    def __fun2(self):
        print('two __')
        
    def show(self):
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)
        
stu = Student('cmm', 29, 'girl')
print(stu._name)
# print(stu.__age)
print(stu._fun1())
print(stu._Student__age)
print(stu._Student__fun2())