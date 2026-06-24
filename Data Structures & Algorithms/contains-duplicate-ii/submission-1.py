from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        c=Counter()
        for j in range(len(nums)):
            c[nums[j]]+=1
            if c[nums[j]]>1:
                return True
            if j-i+1==k+1:
                c[nums[i]]-=1
                if c[nums[i]]==0:
                    del c[nums[i]]
                i=i+1
        return False
        
