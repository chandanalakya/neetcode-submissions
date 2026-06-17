class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=1
        while i<len(nums):
            a=target-nums[i]
            if a in nums[i+1:]:
                return [i,nums.index(a,i+1)]
            else:
                i=i+1
        
            
