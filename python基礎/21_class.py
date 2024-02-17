class Student:
    school = "東京理科大学"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f'私は:{self.name},{self.age}歳です。')
        
    @staticmethod
    def sm():
        print('staticです。')
        
    @classmethod
    def cm(cls):
        print('classmethodです。')
        
stu = Student('ysj', 18)
print(stu.name, stu.age)
print(Student.school)
stu.show()
Student.cm()
Student.sm()