# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        curr=head
        count=0
        while curr!=None:
            curr=curr.next
            count=count+1
        if n==count:
            head=head.next
            return head
        curr1=head
        for i in range(count-n-1):
            curr1=curr1.next
        if curr1 and curr1.next:
            curr1.next=curr1.next.next
        return head

