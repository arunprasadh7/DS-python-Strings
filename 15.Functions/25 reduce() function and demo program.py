#reduce() function and demo program
"""
reduce function reduces the elements from the given sequence into a single element
Its not an inbuilt function & must be imported from functools module inorder to be used in code
we can use import reduce or import *
"""
from functools import reduce #or import *
l = [1,2,3,4,5]

result = reduce(lambda x,y:x+y,l)
print(result)

result = reduce(lambda x,y:x*y,l)
print(result)

result = reduce(lambda x,y:x-y,l)
print(result)

result = reduce(lambda x,y:x/y,l)
print(result)

result = reduce(lambda x,y:x%y,l)
print(result)

result = reduce(lambda x,y:x**y,l)
print(result)

#find sum of first 100 numbers using reduce method

#1-normal way
l1 = []
for i in range(0,101):
    l1.append(i)

sum100Numbers = reduce(lambda x,y:x+y,l1)
print(sum100Numbers)

#2- single line

result = reduce(lambda x,y:x+y,range(1,101))
print(result)
