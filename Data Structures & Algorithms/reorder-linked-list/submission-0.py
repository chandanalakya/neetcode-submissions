# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow.next
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        slow.next=None
        curr1=head
        curr2=prev
        while curr1!=None and curr2!=None:
            next1=curr1.next
            next2=curr2.next
            curr1.next=curr2
            curr2.next=next1
            curr1=next1
            curr2=next2
        

