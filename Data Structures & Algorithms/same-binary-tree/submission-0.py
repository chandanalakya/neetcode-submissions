# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self,root):
        ans=[]
        if root is None:
            return [None]
        ans.append(root.val)
        ans+=self.preorder(root.left)
        ans+=self.preorder(root.right)
        return ans

        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.preorder(p)==self.preorder(q):
            return True
        else:
            return False