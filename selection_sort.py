# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:59:29 2020

@author: Amey
"""

list1=[6000,1,5,2,7,1,8,2,7,5,9,0,1,213,134,224,2566,45335,13,21]

for j in range(0,len(list1)):
    for i in range(j,len(list1)):
        min1=list1[j]
        if list1[i]<=min1:
            min1=list1[i]
            a=list1[i]
            b=list1[j]
            list1[j]=a;
            list1[i]=b;

        