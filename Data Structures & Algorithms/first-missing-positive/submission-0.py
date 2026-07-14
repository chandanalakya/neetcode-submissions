class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>0 and nums[i] <= len(nums):
                a=nums[i]-1
                while nums[i]>0 and nums[i] <= len(nums) and nums[i]!=i+1 and nums[i]!=nums[a]:
                    a=nums[i]-1
                    nums[i],nums[a]=nums[a],nums[i]
        for j in range(len(nums)):
            if nums[j]!=j+1:
                return j+1
        return len(nums)+1


        