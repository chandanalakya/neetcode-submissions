class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        
           
        for j in range(len(nums)):
            a=target-nums[j]
            if a in d and d[a]!=j:
                return [d.get(a),j]
            else:
                d[nums[j]]=j

        