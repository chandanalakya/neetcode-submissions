class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=float("-inf")
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            if s>mx:
                mx=s
            if s<0:
                s=0
        return mx
            
            


        