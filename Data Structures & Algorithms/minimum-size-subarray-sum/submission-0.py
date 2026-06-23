class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        sum=0
        mn=float("inf")
        for j in range(len(nums)):
            sum+=nums[j]
            while sum>=target:
                mn=min(mn,j-i+1)
                sum-=nums[i]
                i=i+1
        return 0 if mn==float("inf") else  mn

