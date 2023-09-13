#Internal tracing of recursive function execution
import math
def fact(n):
    print(f'Executing factorial function with n value {n}')
    if n == 0:
        result = 1
    else:
        result = n * math.factorial(n-1)
    print(f'Returning result of factorial {n} is {result}')
    return result

print(fact(5))
