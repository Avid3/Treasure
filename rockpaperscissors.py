# -*- coding: utf-8 -*-
list1=['rock','paper','scissors']
list2=['rock','paper','scissors']
import random 


result=0;
while result==0:
    comp=random.choice(list1);
    user=input('enter your hand  ')
    print(comp)
    if comp==user:
        result=0
    elif comp=='rock' and user=='paper':
        print('user wins')
        result=1;
    elif comp=='scissors' and user=='rock':
        print('user wins')
        result=1
    elif comp=='paper' and user=='scissors':
        print('user wins')
        result=1
    else:
        print('comp wins')
        result=1
        
        
        
        
    
    






