# -*- coding: utf-8 -*-
#create file wordlist contain names of people
#from said world list split into 2 teams
#if odd number of people give option to user based on input
#team 1 team 2
import random
list1=['tom','dick','harry','ronny','mahesh','ramesh']
team1=list()
for x in range(int(len(list1)/2)):
    w=random.randint(1,len(list1)-1)
    team1.append(list1[w])
    list1.remove(list1[w])