#Demo programs to define and use a class

#eg1
class Student:
    '''this is a sample class creation'''
    def __init__(self):
        self.name = 'Arun'
        self.rollno = 6
        self.marks = 94

    def talk(self):
        print(f'My name is {self.name}.')
        print(f'My rollno is {self.rollno}.')
        print(f'My marks is {self.marks}.')

s1 = Student()
print(s1.name)
print(s1.rollno)
print(s1.marks)
s1.talk()

print('-----------------------------------------------------------------------')              
#eg-2

class Students:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print(f'My name is {self.name}.')
        print(f'My rollno is {self.rollno}.')
        print(f'My marks is {self.marks}.')

s2 = Students('Arun',6,94)
s2.talk()
s3 = Students('Prasadh',7,100)
s3.talk()

