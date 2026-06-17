class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]==nums[j]:
                return True
            else:
                j=j+1
                i=i+1
            
        return False
