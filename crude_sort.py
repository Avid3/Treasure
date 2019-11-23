#somehow it works
#team 1 team 2
#bsorting
enter=input('enter length of sequence ')
enter=int(enter)
x=[None]*enter
for i in range(0,enter):
    x[i]=input()
    x[i]=int(x[i])
#now for sorting
i=0
j=0
s=0
w=0
for w in range(0,len(x)):
    for j in range(0,len(x)):
        for i in range(1,len(x)):
            if x[i]<x[i-1]:
                s=x[i]
                x[i]=x[i-1]
                x[i-1]=s
   
   
            
            
