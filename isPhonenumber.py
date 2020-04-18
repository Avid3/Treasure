# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:01:28 2020

@author: Amey
"""

def isPhonenumber(a):
    import sys
    if len(a)==12:
        if a[3]=='-':
            if a[7]=='-':
                chunk1=a[0:2]
                chunk2=a[4-6]
                chunk3=a[8-11]
                if (chunk1.isdecimal() and chunk2.isdecimal() and chunk3.isdecimal())==False:
                    
                    print('not')
             
                

                else:
                    print('phone number')
                
                            
                    
        
    
