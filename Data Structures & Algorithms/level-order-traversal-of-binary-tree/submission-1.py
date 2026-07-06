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

        ans=[[root.val]]

        while q.size()!=0:

            l=q.size()
            level=[]

            for i in range(l):

                front=q.pop()

                

                if front.left!=None:

                    q.push(front.left)

                    level.append(front.left.val)

                if front.right!=None:

                    q.push(front.right)

                    level.append(front.right.val)
            if level:
                ans.append(level)

        return ans

        



        