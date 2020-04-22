# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:20:45 2020

@author: Amey
"""

def collatz(numbr):
    
    while numbr!=1:
        
        if numbr%2==0:
            numbr=numbr//2
            print(numbr)
        else:
            numbr=3*numbr+1
            print(numbr)