# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:36:16 2020

@author: Amey
"""

def delete_zeros(arr):
    for i in range(0,len(arr)):
        try:
            arr.remove(0)
        except:
            return 
    