"""
Created on Fri Mar 24 09:20:18 2017

@author: Batul Zamin
"""

import math

N = 100

def false_position(func, x0, x1, tolerance):
    """
    Function for regular falsi/ false position method to calculate positive root of equation
    """
    for i in range(1,N+1):
        x2 = x1-(func(x1)*(((x1-x0))/(func(x1)-func(x0))))
        if abs((x2-x1)/x1)<tolerance:
            break
        else:
            if func(x1)*func(x2)<0:
                temp = x1
                x1 = x2
                x0 = temp
            else:
                x1 = x2
    return x2

def f(x):
    return (x**2)-(2*x)-1

def g(x):
    return 5*(math.sin(x))**2-8*(math.cos(x))**5

root1 = false_position(f, 1, 2, 0.0001)
root2 = false_position(g, 0.5, 1.5, 0.000001)

print("Root of Equation 1: "+str(root1))
print("Root of Equation 2: "+str(root2))


