class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            d.update({nums[i]:i})
        
        for j in range(len(nums)):
            a=target-nums[j]
            if a in d and d[a]!=j:
                return [j,d.get(a)]

        