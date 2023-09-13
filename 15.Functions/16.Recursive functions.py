#Recursive functions - a function that calls itself
#uses - can solve complex problems easily - length of code is reduced & redability is reduced

#factorial of number without recursion
def fact(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n-1
    return result
print(fact(5))


#with recursion
import math
def fact1(n):
    if n==0:
        result = 1
    else:
        result = n * math.factorial(n-1)
    return result

print(fact1(4))

for i in range(1,11):
    print(f'The factorial of {i} is {math.factorial(i)}')

