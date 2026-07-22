# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st1=[]
        st2=[]
        ans=[]
        if root ==None:
            return []
        st1.append(root)
        while len(st1)!=0:
            for i in range(len(st1)):
                node=st1.pop()
                if node.left!=None:
                    st1.append(node.left)
                if node.right!=None:
                    st1.append(node.right)
                st2.append(node)
        while len(st2)!=0:
            node=st2.pop()
            ans.append(node.val)
        return ans

