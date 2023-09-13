#conclusions of variable length args

#case 1: variable arg at last
def f1(x,*y):   #x - positional arg, y-variable lenght arg
    print(x)
    print(y)

f1(10)  #x=10, y=no value for variable arg-empty tuple
f1(10,20,30,40) #x=10, y= tuple(20,30,40)

#case 2:variable arg at first
#if variable arg is used first then next arg must be specified with keyword args
def f1(*x,y):   #y - positional arg, x-variable lenght arg
    print(x)
    print(y)

#f1(10,20,30,40)    #error as python assumes all 4 values for x
f1(10,20,30,y=40)

#case 3: both variable args
#we cannot use more than 1 variable length arg, causes error
"""
def f1(*x,*y):
    print(x)
    print(y)
"""