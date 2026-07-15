class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=nums[0]
        mn=nums[0]
        ans=mx
        for i in range(1,len(nums)):
            a=mx
            mx=max(nums[i],mn*nums[i],mx*nums[i])
            mn=min(nums[i],mn*nums[i],a*nums[i])
            
            if mx>ans:
                ans=mx
        return ans
