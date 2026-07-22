# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Queue:

    def __init__(self):

        self.queue=[]

    def push(self,x):

        self.queue.append(x)

    def pop(self):

        x=self.queue[0]

        self.queue.pop(0)

        return x

    def size(self):

        return len(self.queue)

    

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=Queue()

        ans=[]
       

        if root is None:

            return ans

        q.push(root)
        while q.size()!=0:
            s=q.size()
            l=[]
            for i in range(s):
                node=q.pop()
                if node.left!=None:
                    q.push(node.left)
                if node.right!=None:
                    q.push(node.right)
                l=l+[node.val]
            ans.append(l)
        return ans
