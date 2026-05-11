#import random

#def tail_recursion(n:{__It__, __sub__}):
    #if n < 1:
       #return n # base case
    
    #print(n)
    #return tail_recursion(n-1) # recursive call

#tail_recursion(5)

#def a(n:{__gt__}):
    #if n > 0:
       #print(f"Inside a: {n}")
        #return b(n-1)
    
    #if n > 0:
        #return(n)
    #else:
        #print(f"Inside a: {n}")
        #return b(n-1)
    

#def b(n:{__gt__}):
    #if n > 0:
        #print(f"Inside b: {n}")
        #return a(n-1)
    
#a(5)

def head_recursion(n):
    if n < 1:
        return n # base case
    
    head_recursion(n-1) # recursive call
    print(n)

