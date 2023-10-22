# Constructors 2
# if required the __init__ method can be called explicitly

class Test:
    def __init__(self):
        print('constructor execution!')


t1 = Test()
t1.__init__()
t1.__init__()
t1.__init__()

# eg 2


class Tests:
    def __init__(self):
        print('no arg constructor.')

    def __init__(self, x):
        print('one arg constructor.')

#whenever we take 2 constructor or methods with same name by default the last one is taken into consideration
#overloading concept is not applicable for constructors or methods in python 

# t1 = Tests()  
t2 = Tests(10)
