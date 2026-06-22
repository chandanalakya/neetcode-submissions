# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        dummy=ListNode(0)
        t=dummy
        for i in range(len(lists)):
            head=lists[i]
            curr=head
            while curr:
                a.append(curr.val)
                curr=curr.next
        a.sort()
        for i in a:
            new=ListNode(i)       
            t.next=new
            t=t.next
        t.next=None
        head=dummy.next
        return head

        


            
            
        