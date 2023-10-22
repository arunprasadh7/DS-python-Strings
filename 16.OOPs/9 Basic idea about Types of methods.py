#Types of methods - instance, static & class
# if the method contains instance variable(self) then it is called instance method
# if the method contains only clas/static variable(cls) then it is called class method

class Student:
    school_name = 'Durgasoft'   #static/class variable

    def __int__(self, name, roll):
        self.name = name    #instance variable
        self.roll = roll

    def getinfo(self):  #instance method
        print(f'Student Name : {self.name}')
        print(f'Roll no : {self.roll}')

    @classmethod
    def getSchoolInfo(cls):
        print(f'School Name : {cls.school_name}')

    def sum(a,b):   #static method -does not make use of instance or class variable
        sum = a+b
        return sum