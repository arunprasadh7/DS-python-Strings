# 21 Local variables

class Test:

    @staticmethod
    def average(list):
        result = sum(list)/len(list)
        print(f'Average is : {result}')

    @staticmethod
    def wish(name):
        for i in range(10):
            print(f'Good Morning, {i+1} {name}')

t1 = Test()
t1.wish('Arun')
t1.average([10,20,30,40])