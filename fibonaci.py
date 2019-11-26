# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:11:07 2019

@author: Patxi
"""


#last 2 numbers are
fib=[0,0,0]
fib[0]=0
fib[1]=1
print(fib[0])
print(fib[1])
for i in range(0,100):
    fib[2]=fib[0]+fib[1]

    print(fib[2])
    fib[0]=fib[1]
    fib[1]=fib[2]
