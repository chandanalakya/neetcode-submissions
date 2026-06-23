from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        a=[]
        dq=deque()

        for j in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[j]:
                dq.pop()
            dq.append(j)
            if dq[0]<i:
                dq.popleft()
            if j - i + 1 == k:
                mx = dq[0]
                a.append(nums[mx])
                i += 1

        return a