"""
Anonymous funtions - lambda functions
syntax
lambda input args : expression
Nameless function
instant use/one time use
"""

#function to find square of number

#1 - normal method
def sqrt(n):
    square = n*n
    return square

print(sqrt(5))

#2 - lambda method

lambda n : n*n
#lets assign lambda to variable to check its output
s = lambda n : n*n
print(s(4))

s1 = lambda n:n*n*n
for i in range(1,11):
    print(f'The cube of {i} is {s1(i)}')