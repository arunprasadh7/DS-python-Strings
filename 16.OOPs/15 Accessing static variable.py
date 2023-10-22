# 15 Accessing static variable
# inside constructor using self or class name

class Test:
    a  = 10
    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

t1 = Test()
t1.m1()
t1.m2()
t1.m3()