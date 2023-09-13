#filter function demo programs

l = [0,1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda n:n%2==0,l))
print(even)

odd = list(filter(lambda n :n%2!=0,l))
print(odd)

 #numbers divisible by 3 and odd
d3 = list(filter(lambda n:n%3==0 and n%2!=0,l))
print(d3)

#find names starting with k 
l1 = ['Katrina', 'Kareena','Anushka','Deepika','Sunny','Malavika','Arun']

withK = list(filter(lambda name:name[0] == 'K',l1))
print(withK)

#name length divisible by 5

dby5 = list(filter(lambda name:len(name)%5==0,l1))
print(dby5)

#name length is odd

nodd = list(filter(lambda name:len(name)%2!=0,l1))
print(nodd)
