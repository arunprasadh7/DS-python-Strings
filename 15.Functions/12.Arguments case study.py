#different types of args case study

def f1(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)


f1(3,2) #default values will be assigned for args 3 and 4
f1(10,20,30,40) #default values will be overwritten for args 3&4
f1(25,50,arg4=100)  #default value assigned for arg3
f1(arg4=2,arg1=3,arg2=4) #order is not important for keyword args

#invalid types - throws error
"""
f1() - error as 2 positional args are missing
f1(arg3=10,arg4=20,30,40)   #keyword args must be placed atlast
"""