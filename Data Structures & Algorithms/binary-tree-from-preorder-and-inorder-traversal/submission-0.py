# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        pre=0
        for i in range(len(inorder)):
            d[inorder[i]]=i
        def dfs(left,right):
            nonlocal pre
            if left>right:
                return None
            root=TreeNode(preorder[pre])
            pre+=1
            mid=d[root.val]
            root.left=dfs(left,mid-1)
            root.right=dfs(mid+1,right)
            return root
        return dfs(0,len(inorder)-1)

