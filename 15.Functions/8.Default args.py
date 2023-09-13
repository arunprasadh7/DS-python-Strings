#Types of arguments - Default arguments
#if we are not passing any values then the default arg value will be considered

def wish(name='Arun'):
    print(f'Hello {name}. You will be a millionaire soon!!')

wish()  #no args given inside wish, default args will be executed
wish('Prasadh') #default arg value will not be executed

#both default & non default arg can be used simultaneously
def wish(name,msg='You\'re lucky'):
    print(f'Hello {name}.{msg}')
wish('Arun')

#after default arg we cant take non default arg
#def wish(name='Arun',msg):
    #print(f'Hello {name}.{msg}')    #error
