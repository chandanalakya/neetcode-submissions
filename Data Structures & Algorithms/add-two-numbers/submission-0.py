# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        len1=0
        len2=0
        dummy=ListNode(0)
        t=dummy
        s=0
        c=0
        while curr1!=None and curr2!=None:
            s=c+curr1.val+curr2.val
            sum=s%10
            c=s//10
            new=ListNode(sum)
            t.next=new
            t=t.next
            curr1=curr1.next
            curr2=curr2.next
        while curr1!=None:
            s=c+curr1.val
            sum=s%10
            c=s//10
            new=ListNode(sum)
            t.next=new
            t=t.next
            curr1=curr1.next
        while curr2!=None:
            s=c+curr2.val
            sum=s%10
            c=s//10
            new=ListNode(sum)
            t.next=new
            t=t.next
            curr2=curr2.next
        if c!=0:
            new=ListNode(c)
            t.next=new
            t=t.next
        t.next=None
        return dummy.next

            