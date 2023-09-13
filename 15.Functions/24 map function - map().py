# map function - map() - for every values maps a new value
"""
we can use filter() to filter some values based on some condition - function arg is responsible to perform conditional check
map - for every element present in the given sequence apply some function and generate new element with required modification
#syntax - map(function, sequence)
"""

l = [1,2,3,4,5]

#function to find square 
def sqr(n):
    return n*n

#map fun
s1 = list(map(sqr,l))
print(s1)

#using map with lambda
s2 = list(map(lambda n : n*n,l))
print(s2)

#map can take multiple squences
l1 = [1,2,3,4,5,]
l2 = [5,10,15,20,25]

s3 = list(map(lambda x,y : x*y,l1,l2))  #2 sequ x and y
print(s3)

#extra values will be ignored

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [5,10,15,20,25,30]

s4 = list(map(lambda x,y : x*y,l1,l2))  # l1 has 9 values but l2 has only 6 values - output will be executed only for 6
print(s4)

#map with 3 sequence
l1 = [1,2,3,4,5]
l2 = [5,10,15,20,25]
l3 = [10,20,30,40,50]

s5 = list(map(lambda x,y,z : x+y+z ,l1,l2,l3))
print(s5)
