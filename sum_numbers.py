

i=0
length=input('length of array ')
length=int(length)
x=[None]*length
for i in range(0,length):
    x[i]=input()
i=0
sum=0
for i in range(0,len(x)):
    sum=sum+int(x[i])
print(sum)