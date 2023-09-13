#Maximum recursion depth in python
#maximum recursino depth allowed in python 3.6 is 995

count = 0
def factorial(n):
    global  count
    count += 1
    print('Executing factorial function with n value',n)
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)
    return  result

print(factorial(994))
print(count)