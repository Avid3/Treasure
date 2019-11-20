
n=input('enter target')
n=int(n)
x=[1,2,3,4]
y=[3,6,7,8]
lst=[None]*int(len(x))
i=0
j=0
for i in range(0,len(x)):
    for j in range(0,len(y)):
        sum=x[i]+y[j]
        
        if sum==n:
            print(i+1,j+1)
            lst[j]=[j,i]
lst.reverse();
val=0;
res=[]
for val in lst: 
    if val != None : 
        res.append(val) 
def remove_reversed_duplicates(iterable):
    # Create a set for already seen elements
    seen = set()
    for item in iterable:
        # Lists are mutable so we need tuples for the set-operations.
        tup = tuple(item)
        if tup not in seen:
            # If the tuple is not in the set append it in REVERSED order.
            seen.add(tup[::-1])
            # If you also want to remove normal duplicates uncomment the next line
            # seen.add(tup)
            yield item
            
res=list(remove_reversed_duplicates(res))
    
    