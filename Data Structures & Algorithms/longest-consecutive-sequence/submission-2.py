class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx=0
        
        s=set(nums)
        for i in nums:
            count=0
            if i-1 not in s:
                count=1
            while i+count in s:
                count+=1
            mx=max(mx,count)
        return mx
