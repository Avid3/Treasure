# -*- coding: utf-8 -*-
"""
Created on Sun May  3 13:39:50 2020

@author: Amey
"""
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
s=0
for i,j in stuff.items():
    print(i,j)
    
    s=s+j
print(s,'items in total')

# update dictionary
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
j=0
for w in dragonLoot:
    
        
    if w in stuff.keys():
        a=int(stuff[w])
        a=a+1
        stuff[w]=a
    if w not in stuff.keys():
        stuff[w]=1
s=0
for i,j in stuff.items():

    print(i,j)
    s=s+j
print(s,'items in total')
