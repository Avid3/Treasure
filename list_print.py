# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:30:14 2020

@author: Amey
"""

spam=['apples','bananas','tofu','cats']

print(str(spam[0])+', ',end='')

for i in range(1,len(spam)-1):
    
    
        print(str(spam[i])+', ',end='')
print('and ',str(spam[len(spam)-1]),end='')
