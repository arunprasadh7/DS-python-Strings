#shorter code by using filter function - filter(function,sequence)
#filter function can take 2 args

#program to filter even numbers in a given list
l = [0,1,2,3,4,5,6,7,8,9,10]

#method1 - without filter function

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

l1 = []
for n in l:
    if isEven(n)== True:
        l1.append(n)

print(l1)

#method2 -using filter function

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

l2 = filter(isEven,l)   #returns filter object, tyecast to list
print(l2)
print(list(l2)) #typecasted filter to list object

#method3 - using lambda with filter

l3 =filter(lambda n:n%2==0,l)
print(list(l3))
