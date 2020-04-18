# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:09:05 2020

@author: Amey
"""
def isPhonenumber(a):
    
    if len(a)==12:
        if a[3]=='-':
            if a[7]=='-':
                chunk1=a[0:2]
                chunk2=a[4:6]
                chunk3=a[8:11]
                if (chunk1.isdecimal() and chunk2.isdecimal() and chunk3.isdecimal())==False:
                    
                    return False
             
                

                else:
                    return True



n=len(s)
phonenumbers=[]
for i in range(0,n-12):
    w=s[i:i+12]
    if isPhonenumber(w)==True:
        phonenumbers.append(w)
        
    