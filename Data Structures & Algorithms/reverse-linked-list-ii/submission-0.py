# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        if left!=1:
            for i in range(left-2):
                curr=curr.next
            t=curr
            curr=curr.next
        else:
            curr=head
        prev=None
        curr2=head
        for k in range(right):
            curr2=curr2.next
        
        for j in range(left,right+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        t1=prev
        t2=prev
        while t1.next!=None:
            t1=t1.next
        if left!=1:
            t.next=t2
        else:
            head=t2
        t1.next=curr2
        return head

