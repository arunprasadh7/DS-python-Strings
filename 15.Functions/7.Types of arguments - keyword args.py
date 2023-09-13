#Positional & Keyword arguments

def sub(a,b):
    print(a-b)

#positional args , order is important
sub(100,50)
sub(50,100)

#keyword args - order isnt important
sub(a=50,b=25)
sub(b=25,a=50)

#both positional & keyword args can be used simultaneously
#positional args must be declared first followed by keyword args
#sub(a=50,25)    #invalid - keyword arg is first
sub(50,b=25)    #valid - positional arg is first