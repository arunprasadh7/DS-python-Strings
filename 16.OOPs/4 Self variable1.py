# The complete postmortem of self variable part 1

class Test:
    def __init__(self):
        print('Address of reference variable is', id(self))

t1 = Test()
print(id(t1))

#eg 2

class Test2:
    def __init__(self):
        print('constructor')
    
    def m1(self,x):
        print(f'value of x is {x}')

t2 = Test2()
t2.m1(10)