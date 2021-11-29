import person
from types import MethodType

class Student(person.Person):
  def __init__(self, name, age) -> None:
    self.name = name;
    self.age = age;


aStudent = Student('zhangsan', 31)

aStudent.run()

print('type=', type(aStudent))
print('aStudent is Person?', isinstance(aStudent, person.Person))
print('aStudent is Student?', isinstance(aStudent, Student))

# 绑定函数

def set_age(self, age: int):
  self.age = age;

aStudent.set_age = MethodType(set_age, aStudent)
aStudent.set_age(44)
print('aStudent=', aStudent.age)


aStudent.sex = '男'
print('sex=', aStudent.sex)

