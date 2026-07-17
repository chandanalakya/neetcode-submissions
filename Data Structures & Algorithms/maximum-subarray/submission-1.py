class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=float("-inf")
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum>mx:
                mx=sum
            if sum<0:
                sum=0
        return mx


        