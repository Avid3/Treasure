# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:42:53 2020

@author: Amey
"""
b='1'
while b!='':
    birthdays={'Andy':'5 March','Sam':'1 Dec','Julie':'17 November','Albert':'6 Dec'};
    
    a=input('Whose birthday do you want to search***/n Space to exit');
    if a=='':
        break

    if a in birthdays:
        print(birthdays[a])
    else:
        print('No information found. Do you have information for [y/n]')
        b=input()
        if b=='n':
            break
        if b=='y':
            birthdays[a]=input()
            print('Updated')
