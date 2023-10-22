#constructor in python 1

class Test:
    def __init__(self):
        print('Constructor created!')

t1 = Test()
t2 = Test()
t3 = Test()

class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

s1 = Student('Arun',7,95)
s2 = Student('Prasadh',6,90)

print(s1.name,s1.rollno,s1.marks)
print(s2.name,s2.rollno,s2.marks)

