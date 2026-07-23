# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx=float("-inf")
        def dfs(root):
            if root is None:
                return 0
            else:
                left=max(0,dfs(root.left))
                right=max(0,dfs(root.right))
                self.mx=max(self.mx,root.val+left+right)
                return root.val+max(left,right)
        dfs(root)
        return self.mx
            
        