class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            a=target-nums[i]
            if a not in d:
                d[nums[i]]=i
            else:
                return [min(i,d.get(a)),max(i,d.get(a))]