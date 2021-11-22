#calculate the nth y of a function y_prime = 2-2*y-e**(-4*x)
from math import e

def f(x,y):
    return 2-2*y-e**(-4*x)


def euler(prev_x,prev_y,step,target):
    prev_y = prev_y + step*f(prev_x,prev_y)   
    prev_x += step # prev_x has to be updated after prev_y is updated

    if round(prev_x, 2) == target: # desired x
        return prev_y # final answer
    else:
        return euler(prev_x,prev_y,step,target) # first iteration will calc x1,y1
    

print(euler(0,1,.1,.5))
