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
        if len(self.queue)==0:
            return -1
        x=self.queue[0]
        self.queue.pop(0)
        return x
    def size(self):
        if len(self.queue)==0:
            return 0
        else:
            return len(self.queue)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=Queue()
        ans=[]
        if root is None:
            return ans
        q.push(root)
        ans.append([root.val])
        while q.size()!=0:
            f=q.size()
            level=[]
            for i in range(f):
                front=q.pop()
                if front.left!=None:
                    q.push(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    q.push(front.right)
                    level.append(front.right.val)
            if len(level)!=0:
                ans.append(level)
        return ans


        