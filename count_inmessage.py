# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:46:06 2020

@author: Amey
"""
message='it was a lovely day in the woods and i went for a walk with my best friend. we had cucumber sandwiches for lunch and on the way back stopped at a sushi place.'
dic1={}
for character in message:
    dic1.setdefault(character,0)
    dic1[character]=dic1[character]+1
    
