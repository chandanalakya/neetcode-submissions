# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,root,mn,mx):
        if root is None:
            return True
        if root.val<mn or root.val>mx:
            return False
        else:
            checkleft=self.check(root.left,mn,root.val-1)
            checkright=self.check(root.right,root.val+1,mx)
            return checkleft and checkright

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        m=self.check(root,float("-inf"),float("inf"))
        return m
        