from sympy import *

import numpy
import math
import sys



x=symbols('x')

#f=input("give f(x)   ")
f=x**2

a=-pi
b=pi

#c=input("number of elements in fourier series ")
s= fourier_series(f,(x,a,b))


a=s.scalex(1).truncate(50)
output="foureier series of f(x)= ",a,"...."
print(output)


