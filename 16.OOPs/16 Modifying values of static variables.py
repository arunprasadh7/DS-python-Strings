# Where can we modify the static variable

class Test:
    a = 10

    def __init__(self): #constructor
        Test.a = 20

    def m1(self):
        Test.a = 30

    @classmethod
    def m2(cls):
        cls.a = 40
        Test.a = 50

    @staticmethod
    def m3():
        Test.a = 60




t1 = Test()
t1.m1()
t1.m2()
t1.m3()

Test.a = 70

print(Test.a)