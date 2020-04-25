# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:37:28 2020

@author: Amey
"""
birthdays={'John':(5,11),'Arti':(1,4)}
name='someone'
while name!='':
    print('Hi ! Whose birthday would you like to search for ?**Press Enter to exit')
    name=input()
    if name in birthdays:
        print('Birthday is',birthdays[name])
        print('\n Enter a new name or press Enter to exit')
    if name not in birthdays:
        if name=='':
            break
        print('Would you like to update and add birthday information for '+name+' Press Y for Yes and N for No')
        decision=input()
        if decision=='Y':
            print('enter birthday as a tuple')
            birthdays[name]=input()
            print('Do you want to continue ?')
            decision=input()
            if decision=='Y':
                continue
            if decision=='N':
                break
        if decision=='N':
            continue
        else:
            continue
        

