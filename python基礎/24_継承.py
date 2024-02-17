class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'私は{self.name},今年{self.age}歳です。')
            
class Student(Person):
    def __init__(self, name, age, stuno):
        super().__init__(name, age)
        self.stuno = stuno
    def show(self):
        super().show()
        print(f'ナンバーは{self.stuno}')
        
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    def show(self):
        super().show()
        print(f'私は{self.department}です。')
        
stu = Student('cmm', 20, '1001')
stu.show()

doctor = Doctor('wyy', 32, '内科')
doctor.show()