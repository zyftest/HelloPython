# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

setattr(emp1, 'age', 8)  # 添加属性 'age' 值为 8
print(hasattr(emp1, 'age'))  # 如果存在 'age' 属性返回 True。
emp1.age = 7  # 添加一个 'age' 属性
print(getattr(emp1, 'age'))  # 返回 'age' 属性的值
delattr(emp1, 'age')  # 删除属性 'age'

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
    print('当前字母 :', letter)

print("Good bye!")
