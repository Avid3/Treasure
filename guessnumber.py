# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:53:56 2020

@author: Amey
"""

def guess_thenumber():
    import random
    a=random.randint(1,20)
    print('I am thinking of a number between 1 and 20 \n')
    guess=input()
    guesses=0;
    while guess!=a:
        if a>int(guess):
            print('higher')
            guess=input()
            guesses=guesses+1
        if a<int(guess):
            print('lower')
            guess=input()
            guesses=guesses+1
        if a==int(guess):
            print('right on')
            print(guesses+1)
            break
guess_thenumber()

            
            
        