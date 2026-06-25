class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        a=set()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in nums:
            count=d.get(j)
            if count>n//3:
                a.add(j)
        return list(a)

        