"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        o={None:None}
        curr=head
        while curr!=None:
            copy=Node(curr.val)
            o[curr]=copy
            curr=curr.next
        curr=head
        while curr!=None:
            copy=o[curr]
            copy.next=o[curr.next]
            copy.random=o[curr.random]
            curr=curr.next
        return o[head]