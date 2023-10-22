# Types of variables instance, static & local.
"""
instance - obj level variable - differs from obj ot obj
static - class level variable -entire class only one copy
local - method level variable
"""


class Student:

    schoolName = 'Durgasoft'  # static - class level variable

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable

    def info(self):
        x = 10  # x is local variable
        for i in range(x):  # i is local variable
            print(i)

s1 = Student('arun',77)
s1.info()