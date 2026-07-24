# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root,p,path):
            if root is None:
                return False
            path.append(root)
            if root.val==p.val:
                return True
            left=dfs(root.left,p,path)
            right=dfs(root.right,p,path)
            if left or right:
                return True
            path.pop()
            return False
        path1=[]
        path2=[]
        l=dfs(root,p,path1)
        r=dfs(root,q,path2)
        
        ans = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                ans = path1[i]
            else:
                break
        print([x.val for x in path1])
        print([x.val for x in path2])
        return ans
        