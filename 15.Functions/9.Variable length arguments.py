#Variable length arguments - ypu can pass any number of values for that args

def f1(*n):
    print('Variable length argument function')

f1()    #0 args
f1(10)  #1 args
f1(10,20)    #2args
f1(10,20,30)    #3args

#program to find sum  using variable lenght

def sum(*n):
    total = 0
    for i in n:
        total = total + i
    print(f'Sum is {total}.')

sum(1,2,3)
sum(5,5,5,5,5,55,5,5,5,5,5,5)

#case 1

def f2(*n):
    print(n)

f2(10,20,30)    #tuple is created
f2((10,20,30),(40,50,60))   #tuple of tuple is created

