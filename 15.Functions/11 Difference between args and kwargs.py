#difference btwn *args and **kwargs

# *args
# - variable length args
# - f1(*n) - tuple will be created
# eg:
def f1(*n):
    print(n)
f1()    #creates empty tuple
f1(10)
f1(10,20,30)

#kwargs - variable length keyword args
#def f1(**kwargs): - creates dictionary
#eg
def f2(**kwargs):
    print(kwargs)
f2()    #creates empty dict
f2(name = 'Arun',rollno =123)
f2(a=10,b=20,c=30,d=40,e=50)

#*args and **kwargs in one function
#args followed by kwargs is valid
def f3(*args,**kwargs):
    print(args)
    print(kwargs)
f3(10,20,30,a=10,b=20,c=30)

#kwargs followed by args is not allowed
"""
def f4(**kwargs,*args):
    print(kwargs)
    print(args)
"""