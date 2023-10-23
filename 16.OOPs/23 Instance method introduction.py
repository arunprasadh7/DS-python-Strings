# Instance method demo program

class Student:
    '''demo program for instance method'''
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f'Hello, {self.name}.')
        print(f'You\'re marks : {self.marks}')

    def grade(self):
        if self.marks >= 60:
            print('You got First grade')
        elif self.marks >= 50:
            print('You got second grade.')
        elif self.marks >= 35:
            print('You got third grade.')
        else:
            print('You are failed')

print('Enter number of students')
n = int(input())

for i in range(n):
    print('Enter student name:')
    name = input()
    print('Enter student mark:')
    marks = int(input())
    s = Student(name, marks)
    s.display()
    s.grade()
    print()