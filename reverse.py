# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#reverse integer
def reverse(val):
    units=val%10
    tens=val%100
    tens=(tens-units)/10
    hundreds=val%1000
    hundreds=(hundreds-(tens*10+units))/100
    reverse_=units*100+tens*10+hundreds
    print(int(reverse_))
    return(reverse_)
    
    