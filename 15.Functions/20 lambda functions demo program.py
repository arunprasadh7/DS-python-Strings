#lambda functions demo program 

#1-lambda function to find the sum of given 2 numbers

s = lambda a,b:a+b
print(s(2,2))
print(s(10,20))

#2 - to find biggest of two given numbers

bigger = lambda a,b : a if a>b else b
print(bigger(10,20))
print(bigger(-10,-20))

#3 - biggest of 3 numbers
b1 = lambda a,b,c : a if a>b and a>c else b if b>c else c
print(b1(10,20,30))
